from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class VidStream(models.Model):
    streamer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    video = models.FileField(upload_to='')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

class VidRequest(models.Model):
    id = models.IntegerField((""), primary_key=True)
    # auto_increment_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name="user_sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="user_reciever", on_delete=models.CASCADE)
    description = models.TextField(max_length=600)
    due_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
