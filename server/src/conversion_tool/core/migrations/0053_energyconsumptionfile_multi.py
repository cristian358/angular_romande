# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_energyconsumptionfile_meters'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyconsumptionfile',
            name='multi',
            field=models.BooleanField(default=False),
        ),
    ]
