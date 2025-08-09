# profile/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),  # No slash at the start
]
