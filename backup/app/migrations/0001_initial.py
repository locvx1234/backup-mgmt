# Generated by Django 2.0.2 on 2018-02-22 06:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('serial_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('os', models.CharField(max_length=45)),
                ('ip_address', models.GenericIPAddressField()),
                ('ram', models.FloatField()),
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
                ('serial_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Computer')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Sync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_time', models.DateTimeField()),
                ('volume_used', models.FloatField()),
            ],
            options={
                'ordering': ('sync_time',),
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id_volume', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for volume', primary_key=True, serialize=False)),
                ('capacite', models.FloatField()),
                ('serial_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Computer')),
            ],
        ),
        migrations.AddField(
            model_name='sync',
            name='id_volume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Volume'),
        ),
    ]
