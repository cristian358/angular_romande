# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-02 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0004_cockpitoffer_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cockpitoffer',
            name='date_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cockpitoffer',
            name='date_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
