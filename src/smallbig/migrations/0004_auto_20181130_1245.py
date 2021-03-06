# Generated by Django 2.0.9 on 2018-11-30 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smallbig', '0003_auto_20181122_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlordrent',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlord_rents', to='household.Member', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='landlordrent',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='landlord_rents', to='household.Year', verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='landlordretire',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlord_retires', to='household.Member', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='landlordretire',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='landlord_retires', to='household.Year', verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_tenants', to='household.Member', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owners_tenants', to='household.Member', verbose_name='Landlord'),
        ),
        migrations.AlterField(
            model_name='tenanttransfer',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_transfers', to='household.Member', verbose_name='Member'),
        ),
        migrations.AlterField(
            model_name='tenanttransfer',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tenant_transfers', to='household.Year', verbose_name='Year'),
        ),
    ]
