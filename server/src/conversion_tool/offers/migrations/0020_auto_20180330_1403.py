# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-30 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0019_auto_20180330_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(blank=True, choices=[(b'indicative', b'Offre indicative'), (b'signer', b'Offre A signer'), (b'signee', b'Offre signee'), (b'supprimer', b'A supprimer')], default=b'indicative', max_length=255, null=True),
        ),
    ]
