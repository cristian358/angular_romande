# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-08 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20170824_1403'),
        ('core', '0043_energyconsumptionreport_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumDiffReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('datetime_from', models.DateTimeField()),
                ('datetime_to', models.DateTimeField()),
                ('report_file', models.FileField(blank=True, null=True, upload_to=b'')),
                ('meters', models.ManyToManyField(blank=True, related_name='meters', to='companies.Meter')),
                ('shedules', models.ManyToManyField(related_name='sum_shedules', to='core.Shedule')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
