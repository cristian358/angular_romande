# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-13 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_sumdiffreport_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetreport',
            name='pfc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='budgetreport',
            name='unit',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
