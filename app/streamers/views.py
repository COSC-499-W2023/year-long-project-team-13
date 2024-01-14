from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserInfoRegistrationForm, UserUpdateForm, UserInfoUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm, SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import Notification
from django.dispatch import Signal
from . models import Profile, UserInfo

# Define the signal
user_signed_up = Signal()
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        # infoform = UserInfoRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user_signed_up.send(sender=User, user=new_user)
            UserInfo.objects.create(user=new_user, birthdate='2024-01-01')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        # infoform = UserInfoRegistrationForm()
    return render(request, 'streamers/register.html', {"form":form })

@login_required
def profile(request):
    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        personalinfoform = UserInfoUpdateForm(request.POST, instance=request.user.userinfo)
        profileform = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and personalinfoform.is_valid and profileform.is_valid():
            userform.save()
            personalinfoform.save()
            profileform.save()
            return redirect("profile")
    else:
        userform = UserUpdateForm(instance=request.user)
        personalinfoform = UserInfoUpdateForm(instance=request.user.userinfo)
        profileform = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'personalinfoform': personalinfoform,
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
