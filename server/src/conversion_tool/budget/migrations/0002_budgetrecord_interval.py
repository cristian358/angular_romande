# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-15 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetrecord',
            name='interval',
            field=models.DurationField(null=True),
        ),
    ]
