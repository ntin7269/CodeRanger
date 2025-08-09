from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import CodingProblem, SolvedProblem # Use the new model

# Show all problem titles



@login_required
def problem_list(request):
    problems = CodingProblem.objects.all()
    solved_ids = set(
        SolvedProblem.objects.filter(user=request.user)
        .values_list('problem_id', flat=True)
    )
    return render(request, 'problems.html', {
        "problems": problems,
        "solved_ids": solved_ids
    })

def landing_page(request):
    return render(request, 'index.html')


@login_required
def all_problems(request):
    all_problems = CodingProblem.objects.all()
    solved_ids = set(
        SolvedProblem.objects.filter(user=request.user)
        .values_list('problem_id', flat=True)
    )

    context = {
        'all_problems': all_problems,
        'solved_ids': solved_ids
    }
    return render(request, 'all_problems.html', context)

# Show full problem detail after clicking
@login_required
def problem_detail(request, problem_id):
    problem = get_object_or_404(CodingProblem, id=problem_id)

    context = {
        'problem': problem,
    }

    template = loader.get_template('problem_detail.html')
    return HttpResponse(template.render(context, request))
