from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm, SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate, login
from .models import Notification

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'streamers/register.html', {"form":form })

@login_required
def profile(request):
    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        profileform = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect("profile")
    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform,
    }
    return render(request, 'streamers/profile.html', context)

def notifications(request):
    user = request.user
    if user.is_authenticated:
        notifications = Notification.objects.filter(user=user).order_by('-timestamp')
        return render(request, 'streamers/notification.html', {'notifications': notifications})
    else:
        return redirect('streamers:login')  # or wherever you want to redirect unauthenticated users

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print("user:", user)  # and this
        if user is not None:
           Notification.objects.create(user=user, message='You have logged in.')
           login(request, user)
           return redirect('home')  # or wherever you want to redirect after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
    return redirect('home')  # or wherever you want to redirect after logout