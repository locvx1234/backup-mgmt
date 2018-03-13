from __future__ import unicode_literals
from versionfield import VersionField
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
<<<<<<< HEAD
    ram = models.FloatField()
    cpus = models.IntegerField(default=0)
    agent_version = VersionField(default='0.0.0')
=======
    ram = models.IntegerField(help_text="unit MB")
    cpu = models.IntegerField(help_text="the number of cores")
>>>>>>> 50fe28a5a5095002f573da74568e77972940ea0c

    def __str__(self):
        return self.name + " " + str(self.ip_address)

    class Meta:
        ordering = ('name',)


class Volume(models.Model):
    type = models.CharField(max_length=10, help_text="HDD or SSD")
    capacity = models.IntegerField(help_text="unit GB")
    vendor = models.CharField(max_length=200)
    speed = models.IntegerField(help_text="unit rpm")
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.type + " " + self.vendor + " " + str(self.capacity) + "GB " + str(self.speed) + "rpm"


class Schedule(models.Model):
    timestamp = models.DateTimeField()
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.timestamp) + " " + str(self.computer)

    class Meta:
        ordering = ('timestamp',)


class Sync(models.Model):
    sync_time = models.DateTimeField()
    capacity_used = models.FloatField()
    volume = models.ForeignKey('Volume', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.sync_time) + " " + str(self.volume)

    class Meta:
        ordering = ('sync_time',)

