# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-29 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20170918_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translationrecords',
            name='translated_year',
        ),
        migrations.RemoveField(
            model_name='translationrecords',
            name='year',
        ),
    ]
