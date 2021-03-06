# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('articles', '0002_remove_contributor_image'),
        ('home', '0003_aboutpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageTeamLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('position', models.CharField(max_length=120)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Contributor')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='team',
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='aboutpageteamlink',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_team_members', to='home.AboutPage'),
        ),
    ]
