# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-03 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_remove_profile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, b'Admin'), (2, b'Vendeur'), (3, b'Client')], default=2, null=True),
        ),
    ]
