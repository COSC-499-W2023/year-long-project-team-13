from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from PIL import Image, ImageOps
from datetime import date
from django.urls import reverse
from django.core.files.storage import default_storage as storage

# Create your models here.

# Video Request Table
class VidRequest(models.Model):
    id = models.IntegerField((""), primary_key=True)
    # auto_increment_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name="user_sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="user_reciever", on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    due_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.id

    # def get_absolute_url(self):
    #     return reverse("video-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Video Stream Table (Table stores all videos) [Video List table]
class VidStream(models.Model):
    # id = models.OneToOneField(VidRequest, on_delete=models.CASCADE)
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    # video = models.FileField(upload_to='')
    video = models.URLField(max_length=200, default='')


    def __str__(self):
        return self.title
        # return self.id

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

# Contact/Friends Table
# class Contact(models.Model):
#     id = models.IntegerField((""), primary_key=True)
#     sender = models.ForeignKey(User, related_name="user_sender", on_delete=models.CASCADE)
#     reciever = models.ForeignKey(User, related_name="user_reciever", on_delete=models.CASCADE)
#     #     status = models.BooleanField(default=False)


#     def __str__(self):
#         return self.id

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

# Pending friend request table
# class FriendRequset(models.Model):
    # # create a tuple to manage different options for your request status
    # STATUS_CHOICES = (
    #   (1, 'Pending'),
    #   (2, 'Accepted'),
    #   (3, 'Rejected'),
    #  )
    # id = models.IntegerField((""), primary_key=True)
    # sender = models.ForeignKey(User, related_name="requests_sent", on_delete=models.CASCADE)
    # reciever = models.ForeignKey(User, related_name="requests_received", on_delete=models.CASCADE)
    # sent_on = models.DateTimeField(default=timezone.now)

    # # store this as an integer, Django handles the verbose choice options
    # status = models.IntegerField(choices=STATUS_CHOICES, default=1)

#     def __str__(self):
#         return self.id

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

# Post of video table
# class Post(models.Model):
#     id = models.OneToOneField(VidRequest, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE)
#     reciever = models.ForeignKey(User, on_delete=models.CASCADE)
#     sendtime = models.DateTimeField(default=timezone.now)
#     timelimit = models.DateTimeField(default=timezone.now)
#     video = models.FileField(upload_to='')


#     def __str__(self):
#         return self.id

#     def get_absolute_url(self):
#         return reverse("video-detail", kwargs={"pk": self.pk})

# From Streamers
# Update User's Profile Picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="mountain.jpg", upload_to='profile-pics')
    contacts = models.ManyToManyField('self', blank=True)
    notifications = models.TextField(default='', blank=True)

    def __str__(self):
        return f"{self.user.username} Profile "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # fh = storage.open(self.image.url, "wb")
        # format = 'png'  # You need to set the correct image format here
        # self.image.save(fh, format)
        # fh.close()
        # img = Image.open(self.image.path)
        # img.save(self.image.path)
        # fixed_image = ImageOps.exif_transpose(img)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     fixed_image.thumbnail(output_size)
        #     fixed_image.save(self.image.path)

# Update User's First & Last Name
# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

# Update User's Birthdate
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.user.username} PersonalInfo "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# Login Notifications table
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(user_logged_in)
def user_logged_in(sender, user, request, **kwargs):
    Notification.objects.create(user=user, message='You have logged in.')

# Video request notification table
# class VidRequestNotification(models.Model):
#     id = models.OneToOneField(VidRequest, on_delete=models.CASCADE)
#     sender = models.ForeignKey(User, related_name="user_sender", on_delete=models.CASCADE)
#     reciever = models.ForeignKey(User, related_name="user_reciever", on_delete=models.CASCADE)
#     description = models.TextField(max_length=600)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.id

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

# User's Setting preference
class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    darkmode = models.BooleanField(default=False)
    emailnotification = models.BooleanField(default=True)
    # defaultoption =

    def __str__(self):
        return f"{self.user.username} Settings "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


