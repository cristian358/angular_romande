# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-01 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20161201_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daypattern',
            name='weekday',
            field=models.CharField(choices=[(b'monday', b'Monday'), (b'tuesday', b'Tuesday'), (b'wednesday', b'Wednesday'), (b'thursday', b'Thursday'), (b'friday', b'Friday'), (b'saturday', b'Saturday'), (b'sunday', b'Sunday'), (b'public_holiday', b'Public Holiday')], max_length=255),
        ),
        migrations.AlterField(
            model_name='energyconsumptionperiod',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
