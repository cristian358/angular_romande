# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-31 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20170731_1434'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Month',
            new_name='Months',
        ),
    ]