# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 07:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0042_auto_20180504_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='mail_valid',
            new_name='token',
        ),
    ]