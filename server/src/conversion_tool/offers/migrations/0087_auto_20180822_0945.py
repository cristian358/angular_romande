# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0086_auto_20180821_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='eco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='risc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
