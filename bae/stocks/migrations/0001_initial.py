# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=10)),
                ('date_ex', models.DateField()),
                ('open_p', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('high_p', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('low_p', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('close_p', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('volume', models.IntegerField(null=True, blank=True)),
                ('adj_close_p', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date_ex', models.DateField()),
                ('symbol', models.CharField(max_length=10)),
                ('totalshares', models.BigIntegerField(null=True, db_column='totalShares', blank=True)),
                ('totalholders', models.BigIntegerField(null=True, db_column='totalHolders', blank=True)),
                ('newposshares', models.BigIntegerField(null=True, db_column='newposShares', blank=True)),
                ('newposholders', models.BigIntegerField(null=True, db_column='newposHolders', blank=True)),
                ('soldoutposshares', models.BigIntegerField(null=True, db_column='soldoutposShares', blank=True)),
                ('soldoutposholders', models.BigIntegerField(null=True, db_column='soldoutposHolders', blank=True)),
                ('buyersshares', models.BigIntegerField(null=True, db_column='buyersShares', blank=True)),
                ('buyers', models.BigIntegerField(null=True, blank=True)),
                ('sellersshares', models.BigIntegerField(null=True, db_column='sellersShares', blank=True)),
                ('sellers', models.BigIntegerField(null=True, blank=True)),
                ('nextyr', models.FloatField(null=True, blank=True)),
                ('next5yr', models.FloatField(null=True, blank=True)),
                ('meanrecthiswk', models.FloatField(null=True, blank=True)),
                ('meanreclastwk', models.FloatField(null=True, blank=True)),
                ('numbrokers', models.IntegerField(null=True, blank=True)),
                ('shorts', models.FloatField(null=True, blank=True)),
                ('shortsp', models.BigIntegerField(null=True, blank=True)),
                ('shortsc', models.BigIntegerField(null=True, blank=True)),
                ('shortsmove', models.FloatField(null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('companyname', models.CharField(max_length=255, null=True, blank=True)),
                ('rating', models.FloatField(null=True, db_column='RATING', blank=True)),
            ],
            options={
                'db_table': 'sentiment',
            },
        ),
        migrations.CreateModel(
            name='StocksPrice',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=1)),
                ('date_ex', models.DateTimeField()),
                ('open_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('high_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('low_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('close_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('volume', models.IntegerField()),
                ('adj_close_p', models.DecimalField(max_digits=6, decimal_places=4)),
            ],
            options={
                'db_table': 'stocks_price',
            },
        ),
        migrations.CreateModel(
            name='StocksSentiment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('date_ex', models.DateTimeField()),
                ('symbol', models.CharField(max_length=6)),
                ('totalshares', models.IntegerField(db_column='totalShares')),
                ('totalholders', models.IntegerField(db_column='totalHolders')),
                ('newposshares', models.IntegerField(db_column='newposShares')),
                ('newposholders', models.IntegerField(db_column='newposHolders')),
                ('soldoutposshares', models.IntegerField(db_column='soldoutposShares')),
                ('soldoutposholders', models.IntegerField(db_column='soldoutposHolders')),
                ('buyersshares', models.IntegerField(db_column='buyersShares')),
                ('buyers', models.IntegerField()),
                ('sellersshares', models.IntegerField(db_column='sellersShares')),
                ('sellers', models.IntegerField()),
                ('nextyr', models.DecimalField(max_digits=6, decimal_places=2)),
                ('next5yr', models.DecimalField(max_digits=6, decimal_places=2)),
                ('meanrecthiswk', models.DecimalField(max_digits=3, decimal_places=2)),
                ('meanreclastwk', models.DecimalField(max_digits=3, decimal_places=2)),
                ('numbrokers', models.IntegerField()),
                ('shorts', models.DecimalField(max_digits=3, decimal_places=2)),
                ('shortsp', models.IntegerField()),
                ('shortsc', models.IntegerField()),
                ('shortsmove', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=8)),
                ('company_name', models.CharField(max_length=50)),
                ('rating', models.DecimalField(max_digits=12, decimal_places=10)),
            ],
            options={
                'db_table': 'stocks_sentiment',
            },
        ),
        migrations.CreateModel(
            name='StocksSymbol',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('symbol', models.CharField(max_length=6)),
                ('company', models.CharField(max_length=50)),
                ('lastsale', models.DecimalField(max_digits=6, decimal_places=4)),
                ('marketcap', models.IntegerField()),
                ('adrtso', models.IntegerField()),
                ('ipoyear', models.IntegerField()),
                ('sector', models.CharField(max_length=20)),
                ('industry', models.CharField(max_length=50)),
                ('quotelink', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'stocks_symbol',
            },
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.IntegerField(primary_key=True)),
                ('symbol', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('company', models.CharField(max_length=255, null=True, blank=True)),
                ('lastsale', models.DecimalField(null=True, max_digits=10, decimal_places=4, blank=True)),
                ('marketcap', models.BigIntegerField(null=True, blank=True)),
                ('adrtso', models.BigIntegerField(null=True, blank=True)),
                ('ipoyear', models.DecimalField(null=True, max_digits=4, decimal_places=0, blank=True)),
                ('sector', models.CharField(max_length=127, null=True, blank=True)),
                ('industry', models.CharField(max_length=127, null=True, blank=True)),
                ('quotelink', models.CharField(max_length=127, null=True, blank=True)),
            ],
            options={
                'db_table': 'symbol',
            },
        ),
    ]
