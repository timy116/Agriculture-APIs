# Generated by Django 2.0.9 on 2018-11-14 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0004_auto_20180904_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counttype',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Name'),
        ),
    ]