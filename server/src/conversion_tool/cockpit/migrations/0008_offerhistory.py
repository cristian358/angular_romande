# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-07 14:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0047_offer_signed_years'),
        ('pfc', '0007_auto_20180424_1701'),
        ('cockpit', '0007_auto_20180503_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('accepted', models.BooleanField(default=False)),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.Offer')),
                ('pfc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pfc.PFC')),
                ('pfc_market', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pfc.PFCMarket')),
            ],
        ),
    ]