# Generated by Django 3.0.1 on 2019-12-30 23:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('street', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.TextField(default='')),
                ('zipCode', models.TextField(blank=True, null=True)),
                ('stateOrProvince', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('telephone', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('comment', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myrestaurants.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Euro amount')),
                ('date', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(blank=True, null=True, upload_to='myrestaurants')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myrestaurants.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
