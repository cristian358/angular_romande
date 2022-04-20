# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-11 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0078_auto_20180711_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='signer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_signer', to=settings.AUTH_USER_MODEL),
        ),
    ]
