# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-06 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0062_remove_offer_eligible'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='date_debut',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='date_fin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
