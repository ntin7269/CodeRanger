from django.contrib import admin
from .models import CodingProblem, TestCase
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget


class CodingProblemForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = CodingProblem
        fields = '__all__'

class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1
    fields = ['input_data', 'expected_output']

class CodingProblemAdmin(admin.ModelAdmin):
    form = CodingProblemForm
    inlines = [TestCaseInline]
    list_display = ['title']

admin.site.register(CodingProblem, CodingProblemAdmin)
