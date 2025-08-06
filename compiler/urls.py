from django.urls import path
from . import views

app_name = "compiler"  # ✅ so we can namespace urls

urlpatterns = [
    path("ai_review/<int:submission_id>/", views.ai_review, name="ai_review"),
    # other urls...




    path("", views.submit, name="submit"),
]
    