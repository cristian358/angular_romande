# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-30 12:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0021_offer_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 30, 12, 33, 30, 425855)),
        ),
    ]
