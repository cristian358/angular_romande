# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-19 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0006_pfcmarketconsumptionrecord'),
        ('type', '0001_initial'),
        ('offers', '0003_offer_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='pfc',
        ),
        migrations.AddField(
            model_name='offer',
            name='pfc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_pfc', to='pfc.PFC'),
        ),
        migrations.RemoveField(
            model_name='offer',
            name='pfc_market',
        ),
        migrations.AddField(
            model_name='offer',
            name='pfc_market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_market', to='pfc.PFCMarket'),
        ),
        migrations.RemoveField(
            model_name='offer',
            name='profile',
        ),
        migrations.AddField(
            model_name='offer',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_profile', to='type.ProfileType'),
        ),
    ]
