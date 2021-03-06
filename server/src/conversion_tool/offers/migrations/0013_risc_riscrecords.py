# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-23 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0012_offerplot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RiscRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('value', models.FloatField()),
                ('year', models.IntegerField()),
                ('risc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offers.Risc')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
