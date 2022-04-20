# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-24 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_auto_20180123_1616'),
        ('client', '0002_auto_20180124_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
    ]
