# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-24 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20170824_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetconsumptionreport',
            name='budget_meter',
        ),
        migrations.RemoveField(
            model_name='budgetconsumptionreport',
            name='pmeter',
        ),
        migrations.RemoveField(
            model_name='budgetconsumptionreport',
            name='shedules',
        ),
        migrations.DeleteModel(
            name='BudgetConsumptionReport',
        ),
    ]
