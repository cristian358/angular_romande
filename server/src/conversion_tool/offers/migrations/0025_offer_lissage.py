# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-04 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0024_offer_cockpit'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='lissage',
            field=models.BooleanField(default=False),
        ),
    ]
