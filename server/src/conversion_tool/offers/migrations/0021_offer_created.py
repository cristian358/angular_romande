# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-30 12:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0020_auto_20180330_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
