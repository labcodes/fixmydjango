# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-25 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('error_posts', '0012_auto_20160728_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorPostNonPublished',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('error_posts.errorpost',),
        ),
        migrations.CreateModel(
            name='ErrorPostPublished',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('error_posts.errorpost',),
        ),
    ]