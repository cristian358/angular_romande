# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-09 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0015_profile_fonction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fonction',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Account Manager'), (2, 'Key Account Manager'), (3, 'Responsable du service Tarification et Pricing'), (4, 'Responsable March\xe9s'), (5, 'Directeur REC SA'), (6, 'Responsable du Groupe Account Manager'), (7, 'Responsable Qualit\xe9 Ressource Energie'), (8, 'Responsable du March\xe9 Entreprises et Collectivit\xe9s Analyste Pricing'), (9, 'CEO')], default=2, null=True),
        ),
    ]
