# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-13 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20170913_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetreport',
            name='self_unit',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
