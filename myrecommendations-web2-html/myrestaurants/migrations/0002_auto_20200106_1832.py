# Generated by Django 2.2.5 on 2020-01-06 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dishes', to='myrestaurants.Restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='stateOrProvince',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='telephone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='zipCode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
