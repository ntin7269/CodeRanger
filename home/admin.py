# admin.py
from django.contrib import admin
from .models import CodingProblem, TestCase

class TestCaseInline(admin.TabularInline):  # or StackedInline
    model = TestCase
    extra = 1
    fields = ['input_data', 'expected_output']

class CodingProblemAdmin(admin.ModelAdmin):
    inlines = [TestCaseInline]
    list_display = ['title']

admin.site.register(CodingProblem, CodingProblemAdmin)
