from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageOps
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
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
