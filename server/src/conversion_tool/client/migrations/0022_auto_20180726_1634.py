# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0021_profile_last_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_log',
        ),
        migrations.AddField(
            model_name='profile',
            name='log',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
