# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-11 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0010_site_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.Site'),
        ),
    ]
