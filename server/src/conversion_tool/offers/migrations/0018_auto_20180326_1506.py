# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0017_riscrecord_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riscrecord',
            name='default',
        ),
        migrations.AddField(
            model_name='risc',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]
