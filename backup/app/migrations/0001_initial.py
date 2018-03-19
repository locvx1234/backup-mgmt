# Generated by Django 2.0.2 on 2018-03-19 13:54

from django.db import migrations, models
import django.db.models.deletion
import versionfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=45)),
                ('os', models.CharField(max_length=45)),
                ('ip_address', models.GenericIPAddressField()),
                ('agent_version', versionfield.VersionField(default='0.0')),
                ('ram', models.IntegerField(help_text='Unit MB')),
                ('cpu', models.IntegerField(help_text='The number of CPU cores')),
                ('capacity_used', models.FloatField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('issue', models.IntegerField(choices=[(0, 'Schedule'), (1, 'Warning'), (2, 'Error')])),
            ],
            options={
                'ordering': ('email',),
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('computer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Computer')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_time', models.DateTimeField()),
                ('amount_data_change', models.FloatField()),
                ('computer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Computer')),
            ],
            options={
                'ordering': ('-sync_time',),
            },
        ),
    ]
