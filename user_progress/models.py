from django.db import models
from django.contrib.auth.models import User
from home.models import SolvedProblem, CodingProblem
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ranger_name = models.CharField(max_length=50, default="Ranger")

    def total_solved(self):
        return SolvedProblem.objects.filter(user=self.user).count()

    def solved_by_difficulty(self):
        result = {"Easy": 0, "Medium": 0, "Hard": 0}
        problems = CodingProblem.objects.filter(
            id__in=SolvedProblem.objects.filter(user=self.user).values_list('problem_id', flat=True)
        )
        for p in problems:
            if p.difficulty in result:
                result[p.difficulty] += 1
        return result

    





# ✅ Auto-create Profile when a new User is made
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
