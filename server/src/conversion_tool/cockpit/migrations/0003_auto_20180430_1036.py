# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-30 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_headgerecord_schedule'),
        ('cockpit', '0002_auto_20180430_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cockpit',
            name='year',
        ),
        migrations.AddField(
            model_name='cockpit',
            name='weekday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Weekday'),
        ),
    ]
