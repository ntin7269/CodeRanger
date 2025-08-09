from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile
from home.models import CodingProblem

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    total_problems = CodingProblem.objects.count()

    context = {
        "profile": profile,
        "total_problems": total_problems,
        "solved_total": profile.total_solved(),
        "solved_by_diff": profile.solved_by_difficulty(),
    }

    return render(request, "profile.html", context)
