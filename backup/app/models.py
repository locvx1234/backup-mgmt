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
    platform = models.CharField(max_length=100, null=True, blank=True)
    ram = models.FloatField(help_text="Unit GB", null=True, blank=True)
    cpu = models.IntegerField(help_text="The number of CPU cores", null=True, blank=True)
    allowed_capacity = models.FloatField(default=50)
    token = models.CharField(max_length=40)
    key = models.CharField(max_length=44)
    status = models.BooleanField(default=True, help_text="set True to enable backup and vice versa")
    def __str__(self):
        return self.name

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

    DONE = 0
    PROGRESSING = 1
    PENDING = 2
    STOP = 3
    ERROR = 4
    STATUS_BACKUP = (
        (DONE, 'Done'),
        (PROGRESSING, 'Progressing...'),
        (PENDING, 'Pending...'),
        (STOP, 'Stop'),
        (ERROR, 'Error')
    )

    time = models.DateTimeField()
    typeofbackup = models.IntegerField(choices=FREQUENCY)
    status = models.IntegerField(choices=STATUS_BACKUP, default=PENDING)
    ip_server = models.CharField(max_length=21)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.path) + " " + str(self.computer)


class RestoreJob(models.Model):
    DONE = 0
    PROGRESSING = 1
    PENDING = 2
    CANCEL = 3
    ERROR = 4
    STATUS_RESTORE = (
        (DONE, 'Done'),
        (PROGRESSING, 'Progressing...'),
        (PENDING, 'Pending...'),
        (CANCEL, 'Canceled'),
        (ERROR, 'Error')
    )

    computer = models.ForeignKey('Computer', on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=1000)
    backup_id = models.IntegerField()
    time = models.DateTimeField()
    status = models.IntegerField(choices=STATUS_RESTORE, default=PENDING)

    def __str__(self):
        return str(self.path) + " " + str(self.computer)

class DockerRestore(models.Model):
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE, null=True)


class Sync(models.Model):
    sync_time = models.DateTimeField()
    amount_data_change = models.FloatField(help_text="Unit MB")
    computer = models.ForeignKey('Computer', on_delete=models.CASCADE, null=True)
    path = models.CharField(max_length=1000)
    ip_server = models.CharField(max_length=21)
    status = models.CharField(max_length=100)

    def __str__(self):
        return str(self.sync_time) + " " + str(self.computer)

    class Meta:
        ordering = ('-sync_time',)
