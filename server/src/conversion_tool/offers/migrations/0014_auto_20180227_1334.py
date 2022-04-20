# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20180223_1635'),
        ('offers', '0013_risc_riscrecords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='weekdays',
        ),
        migrations.AddField(
            model_name='offer',
            name='offer_type',
            field=models.CharField(blank=True, choices=[(b'Standart', b'Standart'), (b'SME', b'SME')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='riscs',
            field=models.ManyToManyField(blank=True, null=True, related_name='riscs', to='offers.Risc'),
        ),
        migrations.AddField(
            model_name='offer',
            name='shedules',
            field=models.ManyToManyField(blank=True, null=True, related_name='offer_shedules', to='core.Shedule'),
        ),
        migrations.AddField(
            model_name='offer',
            name='unique_prix',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='offer',
            name='unit',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='offer',
            name='validation_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pfc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_pfc', to='pfc.PFC'),
        ),
    ]
