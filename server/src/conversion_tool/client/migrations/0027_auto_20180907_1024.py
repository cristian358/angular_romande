# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-07 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0026_auto_20180815_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth',
            field=models.PositiveSmallIntegerField(blank=True, default=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_auth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]