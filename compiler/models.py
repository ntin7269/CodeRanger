from django.db import models

from home.models import CodingProblem

class CodeSubmission(models.Model):
    problem = models.ForeignKey(CodingProblem, on_delete=models.CASCADE)
    language = models.CharField(max_length=10)
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)  # Optional manual input (e.g., from user)
    output_data = models.TextField(blank=True, null=True)
    verdict = models.CharField(max_length=50, blank=True, null=True)  # Added field for verdict
    submitted_at = models.DateTimeField(auto_now_add=True)