# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-24 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0019_clientlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlog',
            name='log_type',
            field=models.CharField(blank=True, choices=[('open', 'Open Offer Email'), ('click', 'Click Offer Email'), ('send', 'Offer Send Email')], max_length=100, null=True),
        ),
    ]
