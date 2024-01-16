from django.contrib import admin
from . models import Profile, UserInfo, Notification
# , VidRequestNotification, Setting

# Register your models here.
admin.site.register(Profile)

admin.site.register(UserInfo)

admin.site.register(Notification)

# admin.site.register(VidRequestNotification)

# admin.site.register(Setting)
