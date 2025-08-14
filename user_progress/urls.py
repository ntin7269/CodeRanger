# profile/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



urlpatterns = [
    path('', views.profile_view, name='profile_view'),  # No slash at the start
]


