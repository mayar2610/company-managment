# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_structure', '0010_auto_20170705_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manage_structure.Company'),
        ),
    ]
