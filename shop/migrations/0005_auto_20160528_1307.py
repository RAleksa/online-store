# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160528_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='token',
            field=models.CharField(default='79aKaQuRXU3MGaXdFrEKyeaumtsMSmJCpEpSBtsA', max_length=40),
        ),
    ]
