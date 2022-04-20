# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-11 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20170824_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='company_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='company',
            name='function',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='nick',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='surname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='company',
            name='zip_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
