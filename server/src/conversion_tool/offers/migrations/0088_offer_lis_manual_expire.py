# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-23 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0087_auto_20180822_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='lis_manual_expire',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
