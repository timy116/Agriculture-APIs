# Generated by Django 2.0.6 on 2018-08-16 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0002_auto_20180802_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='household',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='member',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='role',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
