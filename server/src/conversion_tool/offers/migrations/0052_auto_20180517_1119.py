# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-17 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0051_auto_20180516_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='risc',
            name='code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='energy_type',
            field=models.CharField(blank=True, choices=[('energy1', 'Hydro Naturemade Star suisse'), ('energy2', 'Hydro suisse'), ('energy3', 'Nucl\xe9aire suisse'), ('energy4', 'Mix hydro-solaire suisse'), ('energy5', 'Hydro Naturemade Star romand'), ('energy6', 'Hydro europ\xe9ens')], max_length=255, null=True),
        ),
    ]
