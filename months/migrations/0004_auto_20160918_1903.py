# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('months', '0003_auto_20160918_1833'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='month',
            unique_together=set([('month', 'year')]),
        ),
    ]