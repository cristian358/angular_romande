# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-05 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0028_auto_20180405_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='lissage_years',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
