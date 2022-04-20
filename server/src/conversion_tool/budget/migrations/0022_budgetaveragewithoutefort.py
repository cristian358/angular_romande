# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-04 12:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0021_budget_lissage'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetAverageWithoutEfort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=255)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='year_without_efort_average_budget', to='budget.Budget')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]