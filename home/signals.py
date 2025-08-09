
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CodeSubmission, SolvedProblem

@receiver(post_save, sender=CodeSubmission)
def mark_as_solved(sender, instance, created, **kwargs):
    if instance.verdict == "Accepted":
        SolvedProblem.objects.get_or_create(user=instance.user, problem=instance.problem)
