# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-21 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0085_max_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='energy_type',
            field=models.CharField(blank=True, choices=[('energy1', 'Certificats hydrauliques suisses naturemade star'), ('energy2', 'Certificats hydrauliques suisses'), ('energy3', 'Certificats nucl\xe9aires suisses '), ('energy4', 'Certificats mix hydrauliques-solaires suisses'), ('energy5', 'Certificats hydrauliques romands naturemade star'), ('energy6', 'Certificats hydrauliques europ\xe9ens'), ('energy7', 'Certificats hydro suisse naturemade basic'), ('energy8', 'Certificats solaire suisse naturemade star'), ('energy9', 'Certificats custom')], max_length=255, null=True),
        ),
    ]
