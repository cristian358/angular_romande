# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-03 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0006_cockpitoffer_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cockpitoffer',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cockpitoffer',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
