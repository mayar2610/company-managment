# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_structure', '0011_auto_20170705_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='manage_structure.Company'),
        ),
    ]
