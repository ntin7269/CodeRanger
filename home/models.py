from django.db import models

class CodingProblem(models.Model):
    title = models.CharField(max_length=255)
    time_limit = models.CharField(max_length=50)
    memory_limit = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)

    description = models.TextField()
    input_constraints = models.TextField()
    output_format = models.TextField()

    sample_input_1 = models.TextField()
    sample_output_1 = models.TextField()
    sample_input_2 = models.TextField(blank=True, null=True)
    sample_output_2 = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# home/models.py

class TestCase(models.Model):
    problem = models.ForeignKey(CodingProblem, on_delete=models.CASCADE, related_name="test_cases")
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)  # Optional: to distinguish sample from hidden

    def __str__(self):
        return f"TestCase for {self.problem.title}"

