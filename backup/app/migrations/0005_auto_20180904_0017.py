# Generated by Django 2.0.2 on 2018-09-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180824_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restorejob',
            name='status',
            field=models.IntegerField(choices=[(0, 'Done'), (1, 'Progressing...'), (2, 'Pending...'), (3, 'Canceled'), (4, 'Error')], default=2),
        ),
    ]
