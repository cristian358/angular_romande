# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-19 10:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20180123_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='function',
            new_name='func',
        ),
    ]
