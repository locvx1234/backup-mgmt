# Generated by Django 2.0.2 on 2018-07-08 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='typeofbackup',
            field=models.IntegerField(choices=[(0, 'Once'), (1, 'Daily'), (2, 'Weekly')]),
        ),
    ]
