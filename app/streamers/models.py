from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from PIL import Image, ImageOps
# import ExifTags

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

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

@receiver(user_logged_in)
def user_logged_in(sender, user, request, **kwargs):
    Notification.objects.create(user=user, message='You have logged in.')

