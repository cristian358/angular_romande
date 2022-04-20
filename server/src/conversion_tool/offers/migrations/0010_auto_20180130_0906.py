# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0009_auto_20180130_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='weekdays',
            field=models.ManyToManyField(blank=True, related_name='offer_weekdays', to='core.Weekday'),
        ),
    ]