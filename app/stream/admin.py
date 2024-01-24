from django.contrib import admin
from . models import VidStream, VidRequest, Profile, UserInfo, Notification, Setting, Post
# , Contact, VidRequestNotification

# Register your models here.
admin.site.register(VidStream)

admin.site.register(VidRequest)

admin.site.register(Post)

# admin.site.register(Contact)

admin.site.register(Profile)

admin.site.register(UserInfo)

admin.site.register(Notification)

# admin.site.register(VidRequestNotification)

admin.site.register(Setting)
