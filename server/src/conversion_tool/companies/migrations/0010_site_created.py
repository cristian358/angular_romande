# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-06 13:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_auto_20180322_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
