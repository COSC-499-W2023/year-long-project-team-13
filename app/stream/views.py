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
from django.core.files.base import ContentFile
from django.conf import settings as aws_settings
import os, subprocess, base64, boto3, time, requests
from stream.storage_backends import MediaStorage, ProfilePictureStorage
from . models import VidRequest, VidStream, Contact, FriendRequest, Post, Profile, UserInfo, Notification, Setting
from . forms import VidUploadForm, VidCreateForm, VidRequestForm, UserRegistrationForm, UserUpdateForm, UserInfoUpdateForm, UserProfileUpdateForm, UserProfileUpdateForm,  ValidatingPasswordChangeForm, AddContactForm, UserPermissionForm, VidRecFilledForm, VidUpFilledForm
# from django.http import HttpResponse


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
            # upload_video.video.delete(save=False)  # Delete the existing video file
            # upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True) # Save into video field with 64 byte content file (video name)

            # Save the video to a temporary file
            temp_video_path = os.path.join(aws_settings.MEDIA_ROOT, 'temp_video.webm')
            with open(temp_video_path, 'wb') as f:
                f.write(decoded_data)

            video_key = f"video_filename.mp4"  # video record file name
            # video_record.mp4

            # Define the output file path
            output_video_path = os.path.join(aws_settings.MEDIA_ROOT, video_key)

            # Convert webm to mp4 using ffmpeg
            try:
                subprocess.run(['ffmpeg', '-i', temp_video_path, '-c', 'copy', output_video_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"FFMPEG Error: {e}")
            # Clean up the temporary file
            os.remove(temp_video_path)

            # Upload video to the input S3 bucket
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY,
                aws_session_token=aws_settings.AWS_SESSION_TOKEN,
                region_name=aws_settings.AWS_S3_REGION_NAME
            )

            if request.POST.get('blurFace') == 'on':  # Check if the checkbox is checked
                s3_bucket_name = aws_settings.AWS_S3_INPUT_BUCKET_NAME  # input s3 bucket for blur face
            else:
                s3_bucket_name = aws_settings.AWS_STORAGE_BUCKET_NAME   # normal output s3 bucket for storage video

            media_storage = MediaStorage()
            video_name = media_storage.get_available_name(name=video_key)   # Check if file exists, if exists increment file name

            with open(output_video_path, 'rb') as video_file:
                s3_client.upload_fileobj(video_file, s3_bucket_name, video_name)    # store the web record converted mp4 to s3

            # Remove the local converted file
            os.remove(output_video_path)

            # Get the URL of the processed video
            processed_video_url = f'https://{aws_settings.CLOUDFRONT_DOMAIN}/{video_name}'

            upload_video.video = processed_video_url    # store cloudfront video url

            upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')

    else:
        createvideoform = VidCreateForm(request.user)

    context = {
        'createvideoform': createvideoform
    }
    return render(request, 'stream/video-create.html', context)

# Function for wait file to finish upload on s3
def wait_for_file_existence(file_url, max_attempts=60, delay=5):
    """
    Function to wait until a file exists in CloudFront distribution.

    Args:
    - file_url: The URL of the file in CloudFront distribution.
    - max_attempts: The maximum number of attempts to check for file existence.
    - delay: The delay (in seconds) between each attempt.

    Returns:
    - True if the file exists within the specified number of attempts, False otherwise.
    """
    for attempt in range(max_attempts):
        response = requests.head(file_url)
        if response.status_code == 200:
            return True
        else:
            print(f"File '{file_url}' does not exist yet. Waiting...")
            time.sleep(delay)
    return False

def upload_video(request):
    if request.method == "POST":
        uploadvideoform = VidUploadForm(request.user, request.POST, request.FILES)
        if uploadvideoform.is_valid():

            # Upload video to the input S3 bucket
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY,
                aws_session_token=aws_settings.AWS_SESSION_TOKEN,
                region_name=aws_settings.AWS_S3_REGION_NAME
            )

            if request.POST.get('blurFace') == 'on':  # Check if the checkbox is checked
                s3_bucket_name = aws_settings.AWS_S3_INPUT_BUCKET_NAME  # input s3 bucket for blur face
            else:
                s3_bucket_name = aws_settings.AWS_STORAGE_BUCKET_NAME   # normal output s3 bucket for storage video

            video_file = request.FILES['video_upload']  # Get video file from input post
            video_key = f"{video_file.name}"  # Store in s3 directory
            media_storage = MediaStorage()
            video_name = media_storage.get_available_name(name=video_key)   # Check if file exists, if exists increment file name

            s3_client.upload_fileobj(video_file, s3_bucket_name, video_name)

            # Get the URL of the processed video
            processed_video_url = f'https://{aws_settings.CLOUDFRONT_DOMAIN}/{video_name}'

            # # Wait until processed video URL exists in CloudFront
            # if wait_for_file_existence(processed_video_url):

            request_id = uploadvideoform.cleaned_data['request_id']

            upload_video = uploadvideoform.save(commit=False)
            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
            upload_video.receiver = receiverfilter

            upload_video.video = processed_video_url    # store cloudfront video url

            upload_video.save()

            # link recent uploaded video request from Post table to Notification table
            recentVideoUpload = Post.objects.filter(sender=request.user).last()

            Notification.objects.create(user=request.user, message=f'You have post a video to '+ str(receiverfilter) +'.', type=5, post_id=recentVideoUpload)
            Notification.objects.create(user=receiverfilter, message=f'You have received a video post from '+ str(request.user) +'.', type=6, post_id=recentVideoUpload)
            return redirect('stream:video-list')

            # else:
            #     # Handle the case where the processed video URL doesn't exist even after waiting
            #     return HttpResponse("Processed video URL is not available yet. Please try again later.")

    else:
        uploadvideoform = VidUploadForm(request.user)

    context = {
        'uploadvideoform': uploadvideoform
    }
    return render(request, 'stream/video-upload.html', context)


def upload_filled_video(request, pk):
    if request.method == "POST":
        uploadvideoform = VidUpFilledForm(request.user, request.POST, request.FILES)
        if uploadvideoform.is_valid():

            # Upload video to the input S3 bucket
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY,
                aws_session_token=aws_settings.AWS_SESSION_TOKEN,
                region_name=aws_settings.AWS_S3_REGION_NAME
            )

            if request.POST.get('blurFace') == 'on':  # Check if the checkbox is checked
                s3_bucket_name = aws_settings.AWS_S3_INPUT_BUCKET_NAME  # input s3 bucket for blur face
            else:
                s3_bucket_name = aws_settings.AWS_STORAGE_BUCKET_NAME   # normal output s3 bucket for storage video

            video_file = request.FILES['video_upload']  # Get video file from input post
            video_key = f"{video_file.name}"  # Store in s3 directory
            media_storage = MediaStorage()
            video_name = media_storage.get_available_name(name=video_key)   # Check if file exists, if exists increment file name

            s3_client.upload_fileobj(video_file, s3_bucket_name, video_name)

            # Get the URL of the processed video
            processed_video_url = f'https://{aws_settings.CLOUDFRONT_DOMAIN}/{video_name}'

            request_id_filter = Notification.objects.get(id=pk).videoRequest_id.id
            request_id = VidRequest.objects.get(id=request_id_filter)

            upload_video = uploadvideoform.save(commit=False)
            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id.id).sender)
            upload_video.receiver = receiverfilter
            upload_video.request_id = request_id

            upload_video.video = processed_video_url    # store cloudfront video url

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


def record_filled_video(request, pk):
    if request.method == "POST":
        createvideoform = VidRecFilledForm(request.user, request.POST, request.FILES)
        if createvideoform.is_valid():

            request_id_filter = Notification.objects.get(id=pk).videoRequest_id.id
            request_id = VidRequest.objects.get(id=request_id_filter)

            upload_video = createvideoform.save(commit=False)

            upload_video.sender = request.user
            receiverfilter = User.objects.get(username=VidRequest.objects.get(id=request_id_filter).sender)
            upload_video.receiver = receiverfilter
            upload_video.request_id = request_id

            # Decode and save the blob data
            blob_data = request.POST['video_blob']  # Get blob video data from html input
            decoded_data = base64.b64decode(blob_data)  # Convert the video data to 64 byte type
            # upload_video.video.delete(save=False)  # Delete the existing video file
            # upload_video.video.save('video_filename.mp4', ContentFile(decoded_data), save=True) # Save into video field with 64 byte content file (video name)

            # Save the video to a temporary file
            temp_video_path = os.path.join(aws_settings.MEDIA_ROOT, 'temp_video.webm')
            with open(temp_video_path, 'wb') as f:
                f.write(decoded_data)

            video_key = f"video_filename.mp4"  # video record file name

            # Define the output file path
            output_video_path = os.path.join(aws_settings.MEDIA_ROOT, video_key)

            # Convert webm to mp4 using ffmpeg
            try:
                subprocess.run(['ffmpeg', '-i', temp_video_path, '-c', 'copy', output_video_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"FFMPEG Error: {e}")
            # Clean up the temporary file
            os.remove(temp_video_path)

            # Upload video to the input S3 bucket
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=aws_settings.AWS_SECRET_ACCESS_KEY,
                aws_session_token=aws_settings.AWS_SESSION_TOKEN,
                region_name=aws_settings.AWS_S3_REGION_NAME
            )

            if request.POST.get('blurFace') == 'on':  # Check if the checkbox is checked
                s3_bucket_name = aws_settings.AWS_S3_INPUT_BUCKET_NAME  # input s3 bucket for blur face
            else:
                s3_bucket_name = aws_settings.AWS_STORAGE_BUCKET_NAME   # normal output s3 bucket for storage video

            media_storage = MediaStorage()
            video_name = media_storage.get_available_name(name=video_key)   # Check if file exists, if exists increment file name

            with open(output_video_path, 'rb') as video_file:
                s3_client.upload_fileobj(video_file, s3_bucket_name, video_name)    # store the web record converted mp4 to s3

            # Remove the local converted file
            os.remove(output_video_path)

            # Get the URL of the processed video
            processed_video_url = f'https://{aws_settings.CLOUDFRONT_DOMAIN}/{video_name}'

            upload_video.video = processed_video_url    # store cloudfront video url

            upload_video.save()

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
    return render(request, 'stream/video-record-filled.html', context)



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

    context = {
        'registrationform': registrationform,
        'userpermissionform': userpermissionform,
    }
    return render(request, 'stream/register.html', context)


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


# Change Password
@login_required
def settings(request):
    if request.method == "POST":
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
