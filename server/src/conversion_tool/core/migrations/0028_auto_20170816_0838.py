# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-16 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_shedule_weekend'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedule',
            name='weekend_days',
            field=models.ManyToManyField(blank=True, related_name='weekend_days', to='core.Weekday'),
        ),
        migrations.AlterField(
            model_name='shedule',
            name='weekdays',
            field=models.ManyToManyField(related_name='weekdays', to='core.Weekday'),
        ),
    ]
