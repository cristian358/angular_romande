# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-12 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_headgerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='headgerecord',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meter_headge_schedule', to='core.Shedule'),
        ),
    ]
