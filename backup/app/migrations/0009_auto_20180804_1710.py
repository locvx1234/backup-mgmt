# Generated by Django 2.0.2 on 2018-08-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180804_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.IntegerField(choices=[(0, 'Done'), (1, 'Progressing...'), (2, 'Pending...')], default=2),
        ),
    ]
