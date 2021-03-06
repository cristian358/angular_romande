# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-15 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_energyconsumptionperiod_energyconsumptionreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('weekday', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(unique=True)),
                ('weekday', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DayPattern')),
            ],
        ),
        migrations.AddField(
            model_name='energyconsumptionperiod',
            name='weekdays',
            field=models.ManyToManyField(to='core.DayPattern'),
        ),
    ]
