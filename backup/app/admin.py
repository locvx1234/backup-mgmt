from django.contrib import admin
from .models import Computer, Sync, Schedule, Notification, RestoreJob

# Register your models here.
admin.site.register(Computer)
admin.site.register(Sync)
admin.site.register(Schedule)
admin.site.register(Notification)
admin.site.register(RestoreJob)
