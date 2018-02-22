from __future__ import unicode_literals

from django.db import models
import uuid


class Notification(models.Model):
    SCHEDULE = 0
    WARNING = 1
    ERROR = 2
    ISSUES = (
        (SCHEDULE, 'Schedule'),
        (WARNING, 'Warning'),
        (ERROR, 'Error')
    )
    email = models.EmailField(max_length=100)
    issue = models.IntegerField(choices=ISSUES)

    def __str__(self):
        return "%s [%s]" % (self.email, self.get_issue_display())

    class Meta:
        ordering = ('email',)


class Computer(models.Model):
    serial_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=45)
    os = models.CharField(max_length=45)
    ip_address = models.GenericIPAddressField()
    ram = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Volume(models.Model):
    id_volume = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for volume")
    capacite = models.FloatField()
    serial_number = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.id_volumeshow 


class Schedule(models.Model):
    timestamp = models.DateTimeField()
    serial_number = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('timestamp',)


class Sync(models.Model):
    sync_time = models.DateTimeField()
    volume_used = models.FloatField()
    id_volume = models.ForeignKey('Volume', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('sync_time',)
