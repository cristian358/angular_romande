# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20161115_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyconsumptionreport',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
    ]