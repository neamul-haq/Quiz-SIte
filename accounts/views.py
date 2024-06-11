from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Change 'home' to your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Change 'home' to your desired redirect URL
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the URL name of your home page

@login_required
def view_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/view_profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

