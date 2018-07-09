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
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=45)
    os = models.CharField(max_length=45, null=True, blank=True)
    ip_address = models.GenericIPAddressField()
    agent_version = VersionField(default="1.0.0")
    ram = models.IntegerField(help_text="Unit MB", null=True, blank=True)
    cpu = models.IntegerField(help_text="The number of CPU cores", null=True, blank=True)
    allowed_capacity = models.FloatField(default=50)

    def __str__(self):
        return self.name + " " + str(self.ip_address)

    class Meta:
        ordering = ('name',)


class Schedule(models.Model):
    ONCE = 0
    DAILY = 1
    WEEKLY = 2
    FREQUENCY = (
        (ONCE, 'Once'),
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    ) 
    time = models.DateTimeField()
    typeofbackup = models.IntegerField(choices=FREQUENCY)
    status = models.BooleanField(default=False)
    ip_server = models.CharField(max_length=21)
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)
    path = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.path) + " " + str(self.computer)


class Sync(models.Model):
    sync_time = models.DateTimeField()
    amount_data_change = models.FloatField()
    computer = models.ForeignKey('Computer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.sync_time) + " " + str(self.computer)

    class Meta:
        ordering = ('-sync_time',)
