# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-28 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
