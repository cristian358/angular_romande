# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_offer_years'),
        ('budget', '0009_auto_20180124_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budget_offer', to='offers.Offer'),
        ),
    ]
