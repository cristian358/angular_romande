# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyConsumptionRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=255)),
                ('interval_start', models.DateTimeField()),
                ('interval', models.DurationField()),
                ('from_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.EnergyConsumptionFile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
