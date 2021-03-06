# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-05 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pfc', '0006_pfcmarketconsumptionrecord'),
        ('offers', '0025_offer_lissage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='ParameterRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='riscrecord',
            name='pfc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risc_pfc', to='pfc.PFC'),
        ),
        migrations.AddField(
            model_name='riscrecord',
            name='pfc_market',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risc_pfc_market', to='pfc.PFCMarket'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pfc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_pfc', to='pfc.PFC'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='pfc_market',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offer_market', to='pfc.PFCMarket'),
        ),
        migrations.AddField(
            model_name='parameterrecord',
            name='offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_offer', to='offers.Offer'),
        ),
        migrations.AddField(
            model_name='parameterrecord',
            name='parameter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter', to='offers.Parameter'),
        ),
    ]
