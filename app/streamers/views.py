from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import UserRegistrationForm, UserUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm, SetPasswordForm
from django.contrib.auth.hashers import make_password

from django.shortcuts import redirect
from django.contrib.auth import logout


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
        # passwordform = SetPasswordForm(request.POST, instance=request.user)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect("profile")
            # user = userform.save(commit=False)
            # user.password = make_password(user.password)
            # user.save()
            # profileform.save()
            # return redirect("profile")

    else:
        userform = UserUpdateForm(instance=request.user)
        profileform = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'profileform': profileform,
    }
    return render(request, 'streamers/profile.html', context)

@login_required
def notifications(request):
    # Here you can add code to fetch and process notifications
    # For now, we'll just render an empty page
    return render(request, 'streamers/notification.html')