# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-03 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0019_budgetmedseasonrecord_budgetmedseasonwithriscsrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetAveragePerYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='year_average_budget', to='budget.Budget')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='BudgetAveragePerYearRiscs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='year_risc_average_budget', to='budget.Budget')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]