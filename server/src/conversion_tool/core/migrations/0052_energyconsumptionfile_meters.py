# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-23 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_meter_company'),
        ('core', '0051_auto_20171229_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyconsumptionfile',
            name='meters',
            field=models.ManyToManyField(blank=True, to='companies.Meter'),
        ),
    ]
