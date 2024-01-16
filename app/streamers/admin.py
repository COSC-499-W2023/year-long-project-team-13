from django.contrib import admin
from . models import Profile, UserInfo, Notification, Setting
# , VidRequestNotification

# Register your models here.
admin.site.register(Profile)

admin.site.register(UserInfo)

admin.site.register(Notification)

# admin.site.register(VidRequestNotification)

admin.site.register(Setting)
