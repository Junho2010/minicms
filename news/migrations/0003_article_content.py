# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170921_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='内容'),
        ),
    ]
