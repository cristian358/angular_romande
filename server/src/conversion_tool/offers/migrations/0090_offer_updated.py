# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-24 09:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0089_offer_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
