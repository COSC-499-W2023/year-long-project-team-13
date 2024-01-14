from django.contrib import admin
from . models import VidStream, VidRequest

# Register your models here.
admin.site.register(VidStream)

admin.site.register(VidRequest)
