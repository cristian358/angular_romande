# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-07 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0028_auto_20180806_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientlog',
            name='log_type',
            field=models.CharField(blank=True, choices=[('open', 'Open Offer Email'), ('click', 'Click Offer Email'), ('send', 'Offer Send Email'), ('signer', 'Click Offer signer'), ('signee', 'Click Offer signee'), ('created', 'Createe Offer'), ('confirmer', 'Confirmer Offer'), ('aconfirmer', 'A Confirmer Offer'), ('refuse', 'Refuse Offer')], max_length=100, null=True),
        ),
    ]
