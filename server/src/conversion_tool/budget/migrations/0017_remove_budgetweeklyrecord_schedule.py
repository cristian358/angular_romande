# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-06 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0016_remove_budgetweeklyrecord_season'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetweeklyrecord',
            name='schedule',
        ),
    ]
