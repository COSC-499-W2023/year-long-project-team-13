from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout, authenticate, login
from django.dispatch import Signal
from django.db.models import Q
from stream.models import UserInfo
from stream.forms import UserInfoUpdateForm

from . models import VidStream, Notification, Profile, UserInfo, Setting, FriendRequest
from . forms import VidUploadForm, VidRequestForm, UserRegistrationForm, UserUpdateForm, UserInfoUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm,  ValidatingPasswordChangeForm, AddContactForm
# SetPasswordFormWithConfirm, SetPasswordForm,

class VideoDetailView(DetailView):
    template_name = "stream/video-detail.html"
    model = VidStream

class GeneralVideoListView(ListView):
    model = VidStream
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']

def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = VidStream.objects.filter(title__contains=query)
            return render(request, 'stream/search.html',{'videos':results})

    return render(request, 'stream/search.html')

def home(request):
    return render(request, 'stream/home.html')

def friendRequest(request):
    if request.method == "POST":
        form = AddContactForm(request.user, request.POST)
        if form.is_valid():
            Notification.objects.create(user=request.user, message=f'You have sent a friend request to '+ str(form.cleaned_data['receiver']) +'.', type=1)
            Notification.objects.create(user=form.cleaned_data['receiver'], message=f'You have received a friend request from '+ str(request.user) +'.', type=2)
            add_contact = form.save(commit=False)
            add_contact.sender = request.user
            add_contact.save()
            return redirect("stream:notifications")
    else:
        form = AddContactForm(request.user)
        search_query = request.GET.get('search', '')
        # Existing users show in alphabetical order
        users = User.objects.filter(Q(username__icontains=search_query) & ~Q(id=request.user.id) & ~Q(requests_sender__receiver=request.user, requests_sender__status=1) & ~Q(requests_receiver__sender=request.user) & ~Q(contact_sender__receiver=request.user) & ~Q(contact_receiver__sender=request.user)).order_by('username')

    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'stream/contact.html', context)

def request_video(request):
    if request.method == "POST":
        form = VidRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stream:home')
    else:
        form = VidRequestForm()
        return render(request, 'stream/request-video.html', {'form':form})


class VideoCreateView(LoginRequiredMixin   ,CreateView):
    model = VidStream
    success_url = "/"
    template_name = 'stream/post-video.html'
    # template_name = 'stream/upload.html'
    fields = ['title', 'description','video']
    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)

class VideoUploadView(LoginRequiredMixin   ,CreateView):
    model = VidStream
    success_url = "/"
    template_name = 'stream/upload.html'
    fields = ['title', 'description','video']
    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = VidStream
    template_name = 'stream/post-video.html'
    success_url = "/"
    fields = ['title','description','video']


    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)
    #this function prevents other people from updating your videos
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False




class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "stream/video-confirm-delete.html"
    success_url = "/"
    model = VidStream

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False



class UserVideoListView(ListView):
    model = VidStream
    template_name = "stream/user_videos.html"
    context_object_name = 'videos'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VidStream.objects.filter(streamer=user).order_by('-upload_date')

#From Streamers
user_signed_up = Signal()
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user_signed_up.send(sender=User, user=new_user)
            UserInfo.objects.create(user=new_user, birthdate='2024-01-01')
            Setting.objects.create(user=new_user, darkmode=False, emailnotification=True)
            return redirect('stream:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'stream/register.html', {"form":form })

@login_required
def profile(request):
    if not hasattr(request.user, 'userinfo'):
        UserInfo.objects.create(user=request.user)
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == "POST":
        userform = UserUpdateForm(request.POST, instance=request.user)
        personalinfoform = UserInfoUpdateForm(request.POST, instance=request.user.userinfo)
        profileform = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if userform.is_valid() and personalinfoform.is_valid() and profileform.is_valid():
            userform.save()
            personalinfoform.save()
            profileform.save()
            return redirect("stream:profile")
    else:
        userform = UserUpdateForm(instance=request.user)
        personalinfoform = UserInfoUpdateForm(instance=request.user.userinfo)
        profileform = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'userform': userform,
        'personalinfoform': personalinfoform,
        'profileform': profileform,
    }
    return render(request, 'stream/profile.html', context)

def notifications(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            if 'deleteFriendRequest' in request.POST:
                # delete the friend request
                # delete notification of sender and receiver friend request
                # make both sender and receiver notification of successful delete the sent friend request

            elif 'acceptFriendRequest' in request.POST:
                # make a contact data with sender and receiver username
                # delete the friend request
                # delete notification of sender and receiver friend request
                # make both sender and receiver notification of successful become friends
            elif 'rejectFriendRequest' in request.POST:
                # delete the friend request
                # delete notification of the sender and receiver friend request
            else:
                notifications = Notification.objects.filter(user=user).order_by('-timestamp')
                return render(request, 'stream/notification.html', {'notifications': notifications})
        else:
            notifications = Notification.objects.filter(user=user).order_by('-timestamp')
            return render(request, 'stream/notification.html', {'notifications': notifications})
    else:
        return redirect('stream:login')  # or wherever you want to redirect unauthenticated users

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         # print("user:", user)  # and this
#         if user is not None:
#         #    Notification.objects.create(user=user, message='You have logged in.')
#         #    login(request, user)
#            return redirect('stream:home')  # or wherever you want to redirect after login
#         else:
#             return render(request, 'stream/login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'stream/login.html')

# def logout_view(request):
#     user = request.user
#     if user.is_authenticated:
#         logout(request)
#     return redirect('stream:home')  # or wherever you want to redirect after logout

# Change Password
@login_required
def settings(request):
    if request.method == "POST":
        # passwordform = SetPasswordForm(request.POST, instance=request.user)
        passwordform = ValidatingPasswordChangeForm(data=request.POST, instance=request.user)

        if passwordform.is_valid():
            new_password1 = passwordform.cleaned_data['password']
            new_password2 = passwordform.cleaned_data['password2']

            # Check if the new passwords match
            if new_password1 == new_password2:
                usertemp = passwordform.save(commit=False)
                usertemp.password = make_password(usertemp.password)
                usertemp.save()
                return redirect("stream:login")

    else:
        passwordform = ValidatingPasswordChangeForm(instance=request.user)

    context = {
        'passwordform': passwordform,
    }
    return render(request, 'stream/settings.html', context)
