# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-03 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0009_auto_20180727_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfc',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
