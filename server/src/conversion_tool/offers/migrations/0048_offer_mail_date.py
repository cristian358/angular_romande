# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0047_offer_signed_years'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='mail_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
