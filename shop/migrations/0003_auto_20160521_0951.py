# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-21 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160521_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='qoute',
            name='qoute',
            field=models.TextField(),
        ),
    ]