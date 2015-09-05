# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20150905_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sentiment',
            name='id',
        ),
        migrations.AlterField(
            model_name='price',
            name='symbol',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='sentiment',
            name='symbol',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
        ),
    ]
