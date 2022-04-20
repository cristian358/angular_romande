# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-03 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0036_remove_offer_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
