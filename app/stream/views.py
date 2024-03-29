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
from stream.forms import UserInfoUpdateForm
from . models import VidRequest, VidStream, Contact, FriendRequest, Post, Profile, UserInfo, Notification, Setting
from . forms import VidUploadForm, VidCreateForm, VidRequestForm, UserRegistrationForm, UserUpdateForm, UserInfoUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm,  ValidatingPasswordChangeForm, AddContactForm, UserPermissionForm, VidRecFilledForm, VidUpFilledForm, SecurityQuestionForm, ResetPasswordForm

import base64
from django.core.files.base import ContentFile
# from background_task import background

class VideoDetailView(DetailView):
    template_name = "stream/video-detail.html"
    model = Post

class GeneralVideoListView(ListView):
    model = Post
    template_name = 'stream/video-list.html'
    context_object_name = 'videos'
    ordering = ['-sendtime']


def search(request):
    if request.method == "POST":
        query = request.POST.get('title', None)
        if query:
            results = Post.objects.filter(title__contains=query)
            return render(request, 'stream/search.html',{'videos':results})

    return render(request, 'stream/search.html')


def home(request):
    return render(request, 'stream/home.html')


def friendRequest(request):
    if request.method == "POST":
        addcontactform = AddContactForm(request.user, request.POST)
        if addcontactform.is_valid():
            add_contact = addcontactform.save(commit=False)
            add_contact.sender = request.user
            add_contact.save()
            # link recent created friendRequest from friend request table to Notification table
            recentFriendRequest = FriendRequest.objects.filter(sender=request.user).last()
            Notification.objects.create(user=request.user, message=f'You have sent a friend request to '+ str(addcontactform.cleaned_data['receiver']) +'.', type=1, friendRequest_id=recentFriendRequest)
            Notification.objects.create(user=addcontactform.cleaned_data['receiver'], message=f'You have received a friend request from '+ str(request.user) +'.', type=2, friendRequest_id=recentFriendRequest)
            return redirect("stream:notifications")
    else:
        addcontactform = AddContactForm(request.user)
        search_query = request.GET.get('search', '')
        # Existing users show in alphabetical order
        users = User.objects.filter(Q(username__icontains=search_query) & ~Q(id=request.user.id) & ~Q(requests_sender__receiver=request.user, requests_sender__status=1) & ~Q(requests_receiver__sender=request.user) & ~Q(contact_sender__receiver=request.user) & ~Q(contact_receiver__sender=request.user) & ~Q(userinfo__permission=request.user.userinfo.permission) & ~Q(userinfo__permission=3)).order_by('username')

    context = {
        'addcontactform': addcontactform,
        'users': users,
    }
    return render(request, 'stream/contact.html', context)


def request_video(request):
    if request.method == "POST":
        requestvideoform = VidRequestForm(request.user, request.POST)
        if requestvideoform.is_valid():
            description = requestvideoform.cleaned_data['description']
            due_date = requestvideoform.cleaned_data['due_date']

            request_video = requestvideoform.save(commit=False)
            request_video.sender = request.user
            request_video.save()
            # link recent created video request from VidRequest table to Notification table
            recentVideoRequest = VidRequest.objects.filter(sender=request.user).last()
            Notification.objects.create(user=request.user, message=f'You have sent a video request to '+ str(requestvideoform.cleaned_data['receiver']) + '.' + '\n\n&nbsp;&nbsp; Video Request ID: ' + str(recentVideoRequest) + '\n&nbsp;&nbsp; Description: ' + description + '\n&nbsp;&nbsp; Due DateTime: ' + due_date.strftime('%Y-%m-%d %H:%M:%S'), type=3, videoRequest_id=recentVideoRequest)
            Notification.objects.create(user=requestvideoform.cleaned_data['receiver'], message=f'You have received a video request from '+ str(request.user) + '.' + '\n\n&nbsp; Video Request ID: ' + str(recentVideoRequest) + '\n&nbsp; Description: ' + description + '\n&nbsp; Due DateTime: ' + due_date.strftime('%Y-%m-%d %H:%M:%S'), type=4, videoRequest_id=recentVideoRequest)
            return redirect('stream:notifications')
    else:
        requestvideoform = VidRequestForm(request.user)

    context = {
        'requestvideoform': requestvideoform
    }
    return render(request, 'stream/request-video.html', context)


class VideoCreateView(LoginRequiredMixin   ,CreateView):
    model = Post
    success_url = "/"
    template_name = 'stream/video-create.html'
    # template_name = 'stream/upload.html'
    form_class = VidCreateForm
    # fields = ['title', 'description','video']
    # ['title','description','timelimit','video','request_id']
    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.sender = self.request.user
        request_id = form.cleaned_data['request_id']
        # form.instance.receiver = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        timelimit = form.cleaned_data['timelimit']
        video = form.cleaned_data['video']
        return super().form_valid(form)


def create_video(request):
    if request.method == "POST":
        createvideoform = VidCreateForm(request.user, request.POST, request.FILES)
        if createvideoform.is_valid():
            request_id = createvideoform.cleaned_data['request_id']

            upload_video = createvideoform.save(commit=False)
            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
            upload_video.receiver = receiverfilter

            # Decode and save the blob data
            blob_data = request.POST['video_blob']  # Get blob video data from html input
            decoded_data = base64.b64decode(blob_data)  # Convert the video data to 64 byte type
            upload_video.video.delete(save=False)  # Delete the existing video file
            upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True) # Save into video field with 64 byte content file (video name)

            upload_video.save()

            # if 'video_blob' in request.POST:  # Check if the video blob exists in the request
            #     blob_data = request.POST['video_blob']  # Get blob video data from HTML input
            #     decoded_data = base64.b64decode(blob_data)  # Convert the video data to bytes
            #     # Delete the existing video file associated with the Post instance
            #     if upload_video.video:
            #         upload_video.video.delete(save=False)
            #     # Save the new video file
            #     upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True)
            #     # upload_video.user.save()

            # upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')

    else:
        createvideoform = VidCreateForm(request.user)

    context = {
        'createvideoform': createvideoform,
        'notification': Notification.objects.filter(user=request.user, type=4)
    }
    return render(request, 'stream/video-create.html', context)

class VideoUploadView(LoginRequiredMixin   ,CreateView):
    model = Post
    success_url = "/"
    template_name = 'stream/video-upload.html'
    fields = ['title', 'description','video']
    # this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

def upload_video(request):
    if request.method == "POST":
        uploadvideoform = VidUploadForm(request.user, request.POST, request.FILES)
        if uploadvideoform.is_valid():

            request_id = uploadvideoform.cleaned_data['request_id']

            upload_video = uploadvideoform.save(commit=False)
            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
            upload_video.receiver = receiverfilter

            # Check if the video file already exists
            # existing_video = Post.objects.filter(video=upload_video.video.name).first()
            # if existing_video:
            #     # Overwrite the existing video file
            #     existing_video.video.delete(save=False)  # Delete the existing video file
            #     upload_video.id = existing_video.id  # Set the ID of the existing video
            upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')
    else:
        uploadvideoform = VidUploadForm(request.user)

    context = {
        'uploadvideoform': uploadvideoform,
        'notification': Notification.objects.filter(user=request.user, type=4)
    }
    return render(request, 'stream/video-upload.html', context)

class VideoUploadFilledView(LoginRequiredMixin   ,CreateView):
    model = Post
    success_url = "/"
    template_name = 'stream/video-upload-filled.html'
    fields = ['title', 'description','video']
    #this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

def upload_filled_video(request, pk):
    if request.method == "POST":
        uploadvideoform = VidUpFilledForm(request.user, request.POST, request.FILES)
        if uploadvideoform.is_valid():

            request_id_filter = Notification.objects.get(id=pk).videoRequest_id.id
            request_id = VidRequest.objects.get(id=request_id_filter)

            upload_video = uploadvideoform.save(commit=False)
            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
            upload_video.receiver = receiverfilter
            upload_video.request_id = request_id

            # Check if the video file already exists
            # existing_video = Post.objects.filter(video=upload_video.video.name).first()
            # if existing_video:
            #     # Overwrite the existing video file
            #     existing_video.video.delete(save=False)  # Delete the existing video file
            #     upload_video.id = existing_video.id  # Set the ID of the existing video
            upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')
    else:
        uploadvideoform = VidUpFilledForm(request.user)

    context = {
        'notification': Notification.objects.filter(id=pk),
        'uploadvideoform': uploadvideoform
    }
    return render(request, 'stream/video-upload-filled.html', context)

class VideoRecordFilledView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    template_name = 'stream/video-record-filled.html'
    success_url = "/"
    fields = ['title','description','timelimit','request_id']

    # this is to make sure that the logged in user is the one to upload the content
    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
    # this function prevents other people from updating your videos
    def test_func(self):
        video = self.get_object()
        if self.request.user == video.sender:
            return True
        return False


def record_filled_video(request, pk):
    if request.method == "POST":
        print("request.method:", request.method)
        createvideoform = VidRecFilledForm(request.user, request.POST, request.FILES)
        if createvideoform.is_valid():
            print("createvideoform.isvalid:", createvideoform.is_valid())
            request_id_filter = Notification.objects.get(id=pk).videoRequest_id.id
            request_id = VidRequest.objects.get(id=request_id_filter)

            upload_video = createvideoform.save(commit=False)

            # upload_video.request_id = request_id
            # upload_video.request_id = Notification.objects.filter(id=pk).first().videoRequest_id.cleaned_data['id']

            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id_filter).sender)
            upload_video.receiver = receiverfilter
            upload_video.request_id = request_id

            # Decode and save the blob data
            blob_data = request.POST['video_blob']  # Get blob video data from html input
            decoded_data = base64.b64decode(blob_data)  # Convert the video data to 64 byte type
            upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True) # Save into video field with 64 byte content file (video name)

            upload_video.save()

            # Check if the video file already exists
            # if 'video_blob' in request.POST:  # Check if the video blob exists in the request
            #     blob_data = request.POST['video_blob']  # Get blob video data from HTML input
            #     decoded_data = base64.b64decode(blob_data)  # Convert the video data to bytes
            #     # Delete the existing video file associated with the Post instance
            #     if upload_video.video:
            #         upload_video.video.delete(save=False)
            #     # Save the new video file
            #     upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True)

            # upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')
        else:
            print(createvideoform.errors)
    else:
        print(request.method)
        createvideoform = VidRecFilledForm(request.user)

    context = {
        'notification': Notification.objects.filter(id=pk),
        'createvideoform': createvideoform
        }
    return render(request, 'stream/video-record-filled.html', context )



class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "stream/video-confirm-delete.html"
    success_url = "/"
    model = Post

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.sender:
            return True
        return False


class UserVideoListView(ListView):
    model = Post
    template_name = "stream/user_videos.html"
    context_object_name = 'videos'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(sender=user).order_by('-sendtime')


user_signed_up = Signal()
def register(request):
    if request.method == "POST":
        registrationform = UserRegistrationForm(request.POST)
        userpermissionform = UserPermissionForm(request.POST)

        if registrationform.is_valid() and userpermissionform.is_valid():
            new_user = registrationform.save()
            user_signed_up.send(sender=User, user=new_user)
            Setting.objects.create(user=new_user, darkmode=False, emailnotification=True)
            userinfo = userpermissionform.save(commit=False)
            userinfo.user = new_user
            userinfo.birthdate = '2024-01-01'
            userinfo.save()
            return redirect('stream:login')
    else:
        registrationform = UserRegistrationForm()
        userpermissionform = UserPermissionForm()
        # usersecurityform = UserSecurityForm()

    context = {
        'registrationform': registrationform,
        'userpermissionform': userpermissionform,
        # 'usersecurityform' : usersecurityform,
        }
    return render(request, 'stream/register.html', context)


def password_reset(request):
    if request.method == 'POST':
        form = SecurityQuestionForm(request.POST)
        if form.is_valid():
            # username = request.POST['username']
            # email = request.POST['email']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            # Check if the user exists with the provided email and username
            try:
                user = User.objects.get(email=email, username=username)
            except User.DoesNotExist:
                messages.error(request, 'User with this email or username does not exist.')
                return redirect('stream:forget-password')

            # Redirect to page to display security question
            return redirect('stream:security-answer', username)

    else:
        form = SecurityQuestionForm()
        # Get the user's security question
        # form = SecurityQuestionForm(security_question=request.user.userinfo.security_question)
    return render(request, 'stream/forget-password.html', {'form': form})


def security_answer(request, username):
    if request.method == 'POST':
        security_answer = request.POST['security_answer']
        user = User.objects.get(username=username)
        # Check if the security answer is correct
        if user.userinfo.security_answer.lower() == security_answer.lower():
            # Redirect to page to reset password
            return redirect('stream:password_reset_done', user)
        else:
            messages.error(request, 'Incorrect security answer.')
            return redirect('stream:security-answer', username)
    return render(request, 'stream/security-answer.html', {'username': UserInfo.objects.filter(user__username=username)})

def password_reset_done(request, username):
    if request.method == "POST":
        # passwordform = SetPasswordForm(request.POST, instance=request.user)
        user = User.objects.get(username=username)
        resetpasswordform = ResetPasswordForm(data=request.POST, instance=user)
        if resetpasswordform.is_valid():
            reset_password = resetpasswordform.cleaned_data['password']
            reset_password2 = resetpasswordform.cleaned_data['password2']
            print("form is valid")

            # Check if the new passwords match
            if reset_password == reset_password2:
                user = resetpasswordform.save(commit=False)
                user.password = make_password(user.password)
                user.save()
                return redirect("stream:login")
            else:
                messages.error(request, 'Passwords do not match.')
                return redirect('stream:password_reset_done', username)
        else:
            messages.error(request, 'Invalid password.')
            print(resetpasswordform.errors)
            return redirect('stream:password_reset_done', username)


    else:
        resetpasswordform = ResetPasswordForm(instance=User.objects.get(username=username))

    context = {
        'passwordform': resetpasswordform, 'username': username
    }
    return render(request, 'stream/password_reset_done.html', context)


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
        'videos': Post.objects.filter(sender=request.user).order_by('-sendtime'),
    }
    return render(request, 'stream/profile.html', context)


def notifications(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            if 'deleteFriendRequest' in request.POST:
                # delete the friend request
                # delete notification of sender and receiver friend request
                # make sender notification of successful delete the sent friend request
                notificationid = request.POST.get('notifID')
                friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
                receiver = FriendRequest.objects.get(id=friendRequestid).receiver
                sender = request.user
                FriendRequest.objects.filter(id=friendRequestid).delete()
                Notification.objects.create(user=sender, message=f'You have successfully deleted a friend request to '+ str(receiver) +'.', type=8)
                return redirect("stream:notifications")
            elif 'acceptFriendRequest' in request.POST:
                # make a contact data with sender and receiver username
                # delete the friend request
                # delete notification of sender and receiver friend request
                # make both sender and receiver notification of successful become friends
                notificationid = request.POST.get('notifID')
                friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
                sender = FriendRequest.objects.get(id=friendRequestid).sender
                receiver = request.user
                Contact.objects.create(sender=sender, receiver=receiver)
                FriendRequest.objects.filter(id=friendRequestid).delete()
                Notification.objects.create(user=sender, message=f'You and '+ str(receiver) +' had become friends.', type=8)
                Notification.objects.create(user=receiver, message=f'You and '+ str(sender) +' had become friends.', type=8)
                return redirect("stream:notifications")
            elif 'rejectFriendRequest' in request.POST:
                # delete the friend request
                # delete notification of the sender and receiver friend request
                # make receiver notification of successful reject friend request
                notificationid = request.POST.get('notifID')
                friendRequestid = Notification.objects.get(id=notificationid).friendRequest_id.id
                sender = FriendRequest.objects.get(id=friendRequestid).sender
                receiver = request.user
                FriendRequest.objects.filter(id=friendRequestid).delete()
                Notification.objects.create(user=receiver, message=f'You have rejected a friend request from '+ str(sender) +'.', type=8)
                return redirect("stream:notifications")
            elif 'deleteVideoRequest' in request.POST:
                # delete the video request
                # delete notification of sender and receiver video request
                # make sender notification of successful delete the sent video request
                notificationid = request.POST.get('notifID')
                videoRequestid = Notification.objects.get(id=notificationid).videoRequest_id.id
                receiver = VidRequest.objects.get(id=videoRequestid).receiver
                sender = request.user
                VidRequest.objects.filter(id=videoRequestid).delete()
                Notification.objects.create(user=sender, message=f'You have successfully deleted a video request to '+ str(receiver) +'.', type=8)
                return redirect("stream:notifications")
            elif 'deleteVideoPost' in request.POST:
                # delete the video post
                # delete notification of sender and receiver video post
                # make sender notification of successful delete the sent video post
                notificationid = request.POST.get('notifID')
                postid = Notification.objects.get(id=notificationid).post_id.id
                receiver = Post.objects.get(id=postid).receiver
                sender = request.user
                Post.objects.filter(id=postid).delete()
                Notification.objects.create(user=sender, message=f'You have successfully deleted a video post to '+ str(receiver) +'.', type=8)
                return redirect("stream:notifications")
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


