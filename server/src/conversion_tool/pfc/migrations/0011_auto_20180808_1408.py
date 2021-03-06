# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-08 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0010_pfc_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfcmarket',
            name='eco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pfcmarket',
            name='file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pfcmarket',
            name='offer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pfcmarket',
            name='opportunite',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pfcmarket',
            name='risc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
