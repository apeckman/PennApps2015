# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_auto_20150905_1650'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StocksPrice',
        ),
        migrations.DeleteModel(
            name='StocksSentiment',
        ),
        migrations.DeleteModel(
            name='StocksSymbol',
        ),
    ]
