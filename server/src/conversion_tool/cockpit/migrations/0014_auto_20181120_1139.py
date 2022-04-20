# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-20 09:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0093_auto_20181001_1132'),
        ('cockpit', '0013_remove_cockpitoffer_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cockpitmarket',
            name='chart',
        ),
        migrations.AddField(
            model_name='chart',
            name='chart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chart',
            name='markets',
            field=models.ManyToManyField(blank=True, to='cockpit.CockpitMarket'),
        ),
        migrations.AddField(
            model_name='chart',
            name='tabel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cockpitmarket',
            name='currency',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cockpitmarket',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cockpitmarket',
            name='unit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cockpitnews',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cockpitnews',
            name='email_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cockpitnews',
            name='emp_news',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cockpitnews',
            name='offers',
            field=models.ManyToManyField(blank=True, related_name='cockpit_offers', to='offers.Offer'),
        ),
        migrations.AddField(
            model_name='cockpitnews',
            name='romande_news',
            field=models.BooleanField(default=False),
        ),
    ]
