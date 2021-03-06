# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-12 13:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20180411_1024'),
        ('core', '0060_seasonrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadgeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('meter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meter_headge', to='companies.Meter')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]
