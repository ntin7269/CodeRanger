
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path("auth/", include("accounts.urls")),
    path("submit/", include("compiler.urls")),
]
