# Generated by Django 2.0.9 on 2018-11-20 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestock', '0005_auto_20181114_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestigationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('code', models.CharField(default='Q', max_length=1, verbose_name='Code')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
        ),
        migrations.AlterModelOptions(
            name='field',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='livestock',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='livestock',
            name='code',
            field=models.CharField(default='default', max_length=12, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='season',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], max_length=1, verbose_name='Season'),
        ),
        migrations.AlterField(
            model_name='livestock',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.Field', verbose_name='Field'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livestock.InvestigationType', verbose_name='Investigation Type'),
        ),
    ]
