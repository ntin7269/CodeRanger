from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from compiler.forms import CodeSubmissionForm
from django.conf import settings
import os
import uuid
import subprocess
from pathlib import Path

from django.http import JsonResponse
from home.models import CodingProblem, TestCase, SolvedProblem 

from .models import CodeSubmission

import google.generativeai as genai
from django.utils import timezone


from dotenv import load_dotenv
load_dotenv()


def ai_review(request, submission_id):
    submission = get_object_or_404(CodeSubmission, id=submission_id)
    code = submission.code
    language = submission.language

    try:
        # Configure AI
        genai.configure(api_key="AIzaSyCegnTdDjnaHhbEDjHm5jTY2giqyVIKd14")
        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        You are an expert programmer. Please review this {language.upper()} code.
        1. Identify logical errors, if any.
        2. Suggest improvements or cleaner versions.
        3. Keep your answer short and practical.

        Code:
        {code}
        """

        response = model.generate_content(prompt)
        ai_review_text = response.text.strip()

    except Exception as e:
        ai_review_text = f"Error fetching AI review: {str(e)}"

    return render(request, "ai_review.html", {
        "submission": submission,
        "ai_review": ai_review_text
    })



def submit(request):
    problem_id = request.GET.get("problem_id")

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)
        action = request.POST.get("action")

        if request.POST.get("ajax") == "true" and action == "run":
            if form.is_valid():
                code = form.cleaned_data["code"]
                language = form.cleaned_data["language"]
                input_data = request.POST.get("sample_input_data", "")
                output = run_code(language, code, input_data)
                return JsonResponse({"output": output})
            else:
                return JsonResponse({"output": "Invalid form data."})


        if form.is_valid():
            form.instance.input_data = request.POST.get("sample_input_data", "")
            submission = form.save()
            code = submission.code
            language = submission.language



            if action == "submit":
                # same as before...
                test_cases = submission.problem.test_cases.all()
                all_passed = True
                full_output = ""

                for i, tc in enumerate(test_cases, 1):
                    result_raw = run_code(language, code, tc.input_data)

                    expected = '\n'.join(line.strip() for line in tc.expected_output.strip().splitlines())
                    result = '\n'.join(line.strip() for line in result_raw.strip().splitlines())

                    if result != expected:
                        status = "❌ Failed"
                        all_passed = False
                        full_output = (
                            f"Test Case #{i}:\n"
                            f"Input:\n{tc.input_data.strip()}\n"
                            f"Expected Output:\n{expected}\n"
                            f"Your Output:\n{result}\n"
                            f"Result: {status}\n"
                        )
                        break

                from django.utils import timezone

                if all_passed:
                    full_output = "✅ All test cases passed."
                    solved, created = SolvedProblem.objects.get_or_create(
                        user=request.user,
                        problem=submission.problem,
                        defaults={"solved_at": timezone.now()}
                    )
                    if not created:
                        # If already solved before, update solved_at to now
                        solved.solved_at = timezone.now()
                        solved.save()


                submission.output_data = full_output
                submission.verdict = "Accepted" if all_passed else "Wrong Answer"
                submission.save()

                return render(request, "result.html", {"submission": submission})

            
            

    else:
        form = CodeSubmissionForm()
        if problem_id:
            form.fields["problem"].initial = problem_id

    return render(request, "compiler.html", {"form": form})

def run_code(language, code, input_data):
    project_path = Path(settings.BASE_DIR)
    directories = ["codes", "inputs", "outputs"]

    for directory in directories:
        dir_path = project_path / directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)

    codes_dir = project_path / "codes"
    inputs_dir = project_path / "inputs"
    outputs_dir = project_path / "outputs"

    unique = str(uuid.uuid4())

    code_file_name = f"{unique}.{language}"
    input_file_name = f"{unique}.txt"
    output_file_name = f"{unique}.txt"

    code_file_path = codes_dir / code_file_name
    input_file_path = inputs_dir / input_file_name
    output_file_path = outputs_dir / output_file_name

    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    if language == "py":
        input_data = input_data.strip()
        if '\n' not in input_data and ' ' in input_data:
            input_data = '\n'.join(input_data.split())
        else:
            input_data = '\n'.join([line.strip() for line in input_data.splitlines() if line.strip()])

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    output_data = ""

    if language == "cpp":
        executable_path = codes_dir / unique
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if compile_result.returncode != 0:
            output_data = compile_result.stderr
        else:
            try:
                run_result = subprocess.run(
                    [str(executable_path)],
                    stdin=open(input_file_path, "r"),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    timeout=5
                )
                if run_result.returncode != 0:
                    output_data = f"Runtime Error (exit code {run_result.returncode}):\n{run_result.stdout}"
                else:
                    output_data = run_result.stdout
            except subprocess.TimeoutExpired:
                output_data = "Error: Code execution timed out."

    elif language == "py":
        try:
            run_result = subprocess.run(
                ["python3", str(code_file_path)],
                stdin=open(input_file_path, "r"),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=5
            )
            output_data = run_result.stdout
        except subprocess.TimeoutExpired:
            output_data = "Error: Code execution timed out."

        # ✅ Write the output to the output file
    with open(output_file_path, "w") as output_file:
        output_file.write(output_data)


    return output_data