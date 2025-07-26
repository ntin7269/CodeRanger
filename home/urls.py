from django.urls import path
from home import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('problems/', views.all_problems, name='all_problems'),
    path('problems/<int:problem_id>/', views.problem_detail, name='problem_detail'),
]


