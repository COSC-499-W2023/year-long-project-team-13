from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from PIL import Image, ImageOps
from datetime import date
# from . models import VidStream, VidRequest
# from stream.models import VidRequest
# import ExifTags

# Update User's Profile Picture
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="mountain.jpg", upload_to='profile-pics')

    def __str__(self):
        return f"{self.user.username} Profile "

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        fixed_image = ImageOps.exif_transpose(img)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            fixed_image.thumbnail(output_size)
            fixed_image.save(self.image.path)

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
