# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-30 08:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offers', '0031_offer_profile_pondere'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cockpit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CockpitOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('highest', models.FloatField(blank=True, null=True)),
                ('lowest', models.FloatField(blank=True, null=True)),
                ('date_from', models.DateTimeField(blank=True)),
                ('date_to', models.DateTimeField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cockpit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cockpit.Cockpit')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='offers.Offer')),
            ],
        ),
    ]
