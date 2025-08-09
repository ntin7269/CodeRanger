# OJ/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path("auth/", include("accounts.urls")),
    path("submit/", include(("compiler.urls", "compiler"), namespace="compiler")),
    path("profile/", include(("user_progress.urls", "user_progress"), namespace="user_progress")),
    path('ckeditor5/', include('django_ckeditor_5.urls')), 
]
