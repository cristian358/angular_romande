# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-14 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_shedule_all_holidays'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedule',
            name='weekend',
            field=models.BooleanField(default=False),
        ),
    ]
