# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-18 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20180411_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]