# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-28 11:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_auto_20180528_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='code',
            new_name='token',
        ),
    ]
