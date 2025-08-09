from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('/auth/register/')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('/auth/register/')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/auth/register/')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()

        messages.success(request, 'User created successfully. Please log in.')
        return redirect('/auth/login/')

    context = {
        'info_message': 'Please register to continue.'
    }
    return render(request, 'register.html', context)


def login_user(request):

    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('/auth/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Incorrect password')
            return redirect('/auth/login/')

        login(request, user)
        
        return redirect('/')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')