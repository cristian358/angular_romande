# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-17 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0005_auto_20180117_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
