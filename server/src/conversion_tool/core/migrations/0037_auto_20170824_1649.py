# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-24 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_remove_budgetconsumptionreport_budget_meter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetconsumptionreport',
            name='meters',
            field=models.ManyToManyField(related_name='meters', to='companies.Meter'),
        ),
    ]
