# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-25 09:46
from __future__ import unicode_literals

from django.db import migrations, models

def load_stores(apps, schema_editor):
    OfferStop = apps.get_model("offers", "OfferStop")
    constants_corporate = OfferStop(id=1)
    constants_corporate.save()


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0059_offerstop'),
    ]

    operations = [
	migrations.RunPython(load_stores),
    ]