# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0002_auto_20160918_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'Febuary'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
    ]