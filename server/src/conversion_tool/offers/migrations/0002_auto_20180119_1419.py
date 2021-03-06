# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-19 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0006_pfcmarketconsumptionrecord'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='pfc',
            field=models.ManyToManyField(related_name='offer_pfc', to='pfc.PFC'),
        ),
        migrations.AddField(
            model_name='offer',
            name='pfc_market',
            field=models.ManyToManyField(related_name='offer_market', to='pfc.PFCMarket'),
        ),
    ]
