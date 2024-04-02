from django.contrib import admin
from . models import VidRequest, VidStream, Contact, FriendRequest, Post, Profile, UserInfo, Notification, Setting

# Make table layout display for admin
class VidRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'description', 'due_date')

class VidStreamAdmin(admin.ModelAdmin):
    list_display = ('id', 'streamer', 'upload_date', 'video')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver')

class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'sent_on', 'status')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'title', 'description', 'sendtime', 'timelimit', 'video','video_id', 'request_id')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image')

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'birthdate', 'permission', 'security_question', 'security_answer')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'timestamp', 'type', 'friendRequest_id', 'videoRequest_id', 'post_id', 'video_id')

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'darkmode', 'emailnotification')


# Register your models here.
admin.site.register(VidRequest, VidRequestAdmin)

admin.site.register(VidStream, VidStreamAdmin)

admin.site.register(Contact, ContactAdmin)

admin.site.register(FriendRequest, FriendRequestAdmin)

admin.site.register(Post, PostAdmin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserInfo, UserInfoAdmin)

admin.site.register(Notification, NotificationAdmin)

admin.site.register(Setting, SettingAdmin)
