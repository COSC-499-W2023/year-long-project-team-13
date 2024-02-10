from django.contrib import admin
from . models import VidRequest, VidStream,  Contact, FriendRequest, Post, Profile, UserInfo, Notification, Setting
# VidRequestNotification
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_id', 'request_id')  
# Register your models here.
admin.site.register(VidRequest)

admin.site.register(VidStream)

admin.site.register(Contact)

admin.site.register(FriendRequest)

admin.site.register(Post, PostAdmin)

admin.site.register(Profile)

admin.site.register(UserInfo)

admin.site.register(Notification)

# admin.site.register(VidRequestNotification)

admin.site.register(Setting)
