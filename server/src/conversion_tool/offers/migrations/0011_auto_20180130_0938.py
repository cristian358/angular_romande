# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0010_auto_20180130_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='consumption',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
