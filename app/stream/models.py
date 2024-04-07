from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from PIL import Image, ImageOps
from datetime import date
from django.urls import reverse
from django.core.files.storage import default_storage as storage
from stream.storage_backends import MediaStorage, ProfilePictureStorage
# Create your models here.

# Video Request Table
class VidRequest(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name="video_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="video_receiver", on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    due_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender} {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Video Stream Table (Table stores all videos) [Video List table]
class VidStream(models.Model):
    id = models.AutoField(primary_key=True)
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

# Contact/Friends Table
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name="contact_sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="contact_receiver", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Pending friend request table
class FriendRequest(models.Model):
    # create a tuple to manage different options for your request status
    STATUS_CHOICES = (
      (1, 'Pending'),
      (2, 'Accepted'),
      (3, 'Rejected'),
     )
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_receiver")
    sent_on = models.DateTimeField(default=timezone.now)

    # store this as an integer, Django handles the verbose choice options
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Post of video table
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_receiver')
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    sendtime = models.DateTimeField(default=timezone.now)
    timelimit = models.DateTimeField(default=timezone.now)
    # video = models.FileField(upload_to='')    # local SQLite
    # video = models.FileField(storage=MediaStorage())    # S3 cloudfront
    video = models.URLField()   # Video url (cloudfront) for more upload to s3 options
    video_id = models.ForeignKey(VidStream, on_delete=models.SET_NULL, null=True)
    request_id = models.ForeignKey(VidRequest, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id}"

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
    #     # Add the user attribute to the File object
    #     # self.video.file.user = self.sender
    #     self.video.sender = self.sender

        # Call the original save method
        super().save(*args, **kwargs)


# Update User's Profile Picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default="mountain.jpg", upload_to='profile-pics')   # local SQLite
    image = models.ImageField(default="mountain.jpg", storage=ProfilePictureStorage())  # S3 cloudfront

    def __str__(self):
        return f"{self.user.username} Profile "

    def save(self, *args, **kwargs):
        self.image.file.user = self.user
        super().save(*args, **kwargs)

        # img = Image.open(self.image.path)
        # fixed_image = ImageOps.exif_transpose(img)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     fixed_image.thumbnail(output_size)
        #     fixed_image.save(self.image.path)


# Update User's Birthdate
class UserInfo(models.Model):
    STATUS_CHOICES = (
      (1, 'Sender'),
      (2, 'Receiver'),
      (3, 'Admin'),
     )
    QUESTIONS_CHOICES = (
      (1, 'What was the name of your first pet?'),
      (2, 'In which city were you born?'),
      (3, 'What is the middle name of your oldest sibling?'),
      (4, 'What is the name of your favorite sports team?'),
      (5, 'What was the make and model of your first car?'),
     )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(default=date.today)
    permission = models.IntegerField(choices=STATUS_CHOICES, default=1)
    security_question = models.IntegerField(choices=QUESTIONS_CHOICES, default=1)
    security_answer = models.CharField(max_length=300, default=' ')

    def __str__(self):
        return f"{self.user.username} PersonalInfo"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Login Notifications table
class Notification(models.Model):
    TYPE_CHOICES = (
      (1, 'Friend Request Send'),
      (2, 'Accept/Reject Friend Request'),
      (3, 'Video Request Send'),
      (4, 'Video Request Receive'), # Go to record video
      (5, 'Post Upload'),
      (6, 'Post Receive'),
      (7, 'Video Upload'),
      (8, 'Text')
     )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.IntegerField(choices=TYPE_CHOICES, null=True)
    friendRequest_id = models.ForeignKey(FriendRequest, on_delete=models.CASCADE, null=True)
    videoRequest_id = models.ForeignKey(VidRequest, on_delete=models.CASCADE, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    video_id = models.ForeignKey(VidStream, on_delete=models.SET_NULL, null=True)
    is_read = models.BooleanField(default=False) # false when notification not read

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def notification_as_list(self):
        return self.message.split('&nbsp;')

# User's Setting preference
class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    darkmode = models.BooleanField(default=False)
    emailnotification = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} Settings"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
