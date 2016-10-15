# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0004_auto_20160918_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='feature_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='feature_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
