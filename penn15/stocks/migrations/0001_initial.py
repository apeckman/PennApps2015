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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=1)),
                ('date_ex', models.DateTimeField()),
                ('open_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('high_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('low_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('close_p', models.DecimalField(max_digits=6, decimal_places=4)),
                ('volume', models.IntegerField()),
                ('adj_close_p', models.DecimalField(max_digits=6, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_ex', models.DateTimeField()),
                ('symbol', models.CharField(max_length=6)),
                ('totalShares', models.IntegerField()),
                ('totalHolders', models.IntegerField()),
                ('newposShares', models.IntegerField()),
                ('newposHolders', models.IntegerField()),
                ('soldoutposShares', models.IntegerField()),
                ('soldoutposHolders', models.IntegerField()),
                ('buyersShares', models.IntegerField()),
                ('buyers', models.IntegerField()),
                ('sellersShares', models.IntegerField()),
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
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
        ),
    ]
