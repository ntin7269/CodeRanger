from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from home.models import CodingProblem  # Use the new model

# Show all problem titles
def landing_page(request):
    return render(request, 'index.html')


def all_problems(request):
    all_problems = CodingProblem.objects.all()

    context = {
        'all_problems': all_problems,
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
