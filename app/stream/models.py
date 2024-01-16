from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
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
    video = models.FileField(upload_to='')


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
