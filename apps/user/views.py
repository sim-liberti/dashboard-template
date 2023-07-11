from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
from apps.booklet.models import Booklet

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {
                'error_message': 'Invalid username or password',
            }
            return render(request, 'user/login.html', context)
            
        login(request, user)
        
        return redirect('homepage')
    return render(request, 'user/login.html', {})

def signup_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(
            first_name=firstname,
            last_name=lastname,
            username=username, 
            email=email, 
            password=password
        )

        if user is None:
            context = {
                'error_message': 'Invalid form',
            }
            return render(request, 'user/logout.html', context)

        profile = Profile(user=user)
        profile.save()

        booklet = Booklet(owner=user)

        return redirect('homepage')
    return render(request, 'user/signup.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'user/logout.html')

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user,}
    return render(request, 'user/profile.html', context)