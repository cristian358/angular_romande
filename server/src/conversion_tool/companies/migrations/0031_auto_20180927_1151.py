# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-27 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0030_smeemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='meter_id',
            field=models.CharField(max_length=255),
        ),
    ]
