# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160528_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_root',
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.CharField(default='95sBaFngEX3dCwjBvpqNIRSMrDNkx5CoSlC9Abt3', max_length=40),
        ),
    ]