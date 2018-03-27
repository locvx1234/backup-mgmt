from django.contrib import admin
from .models import Computer, Sync, Schedule, Notification

# Register your models here.
admin.site.register(Computer)
admin.site.register(Sync)
admin.site.register(Schedule)
admin.site.register(Notification)

