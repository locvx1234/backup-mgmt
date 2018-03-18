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
    serial_number = models.CharField(max_length=50)
    name = models.CharField(max_length=45)
    os = models.CharField(max_length=45)
    ip_address = models.GenericIPAddressField()
    agent_version = VersionField(default='0.0')
    ram = models.IntegerField(help_text="Unit MB")
    cpu = models.IntegerField(help_text="The number of CPU cores")
    capacity_used = models.FloatField()

    def __str__(self):
        return self.name + " " + str(self.ip_address)

    class Meta:
        ordering = ('name',)


class Schedule(models.Model):
    timestamp = models.DateTimeField()
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.timestamp) + " " + str(self.computer)

    class Meta:
        ordering = ('-timestamp',)


class Sync(models.Model):
    sync_time = models.DateTimeField()
    amount_data_change = models.FloatField()
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.sync_time) + " " + str(self.volume)

    class Meta:
        ordering = ('-sync_time',)

