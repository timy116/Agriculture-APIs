# Generated by Django 2.0.6 on 2018-09-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster', '0002_auto_20180904_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
        migrations.AddField(
            model_name='disasterevent',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
    ]
