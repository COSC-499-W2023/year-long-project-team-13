from django.contrib import admin
from . models import VidRequest, VidStream,  Contact, FriendRequset, Post, Profile, UserInfo, Notification, Setting
# VidRequestNotification

# Register your models here.
admin.site.register(VidRequest)

admin.site.register(VidStream)

admin.site.register(Contact)

admin.site.register(FriendRequset)

admin.site.register(Post)

admin.site.register(Profile)

admin.site.register(UserInfo)

admin.site.register(Notification)

# admin.site.register(VidRequestNotification)

admin.site.register(Setting)
