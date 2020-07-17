# Generated by Django 2.0.9 on 2018-11-21 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0007_profile_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livestock',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.Livestock', verbose_name='Parent'),
        ),
    ]
