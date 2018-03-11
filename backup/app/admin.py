from django.contrib import admin
from .models import Computer, Volume, Sync, Schedule, Notification

# Register your models here.
admin.site.register(Computer)
admin.site.register(Volume)
admin.site.register(Sync)
admin.site.register(Schedule)
admin.site.register(Notification)

