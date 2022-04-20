# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0044_remove_offer_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='token',
            field=models.UUIDField(blank=True, default=uuid.uuid4, null=True),
        ),
    ]
