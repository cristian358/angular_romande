# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0007_auto_20180129_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='cc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_cc', to='companies.Meter'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_profile', to='type.ProfileType'),
        ),
    ]
