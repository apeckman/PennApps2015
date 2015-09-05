# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models



class Price(models.Model):
    symbol = models.CharField(max_length=10)
    date_ex = models.DateField()
    open_p = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    high_p = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    low_p = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    close_p = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    adj_close_p = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'price'


class Sentiment(models.Model):
    date_ex = models.DateField()
    symbol = models.CharField(max_length=10)
    totalshares = models.BigIntegerField(db_column='totalShares', blank=True, null=True)  # Field name made lowercase.
    totalholders = models.BigIntegerField(db_column='totalHolders', blank=True, null=True)  # Field name made lowercase.
    newposshares = models.BigIntegerField(db_column='newposShares', blank=True, null=True)  # Field name made lowercase.
    newposholders = models.BigIntegerField(db_column='newposHolders', blank=True, null=True)  # Field name made lowercase.
    soldoutposshares = models.BigIntegerField(db_column='soldoutposShares', blank=True, null=True)  # Field name made lowercase.
    soldoutposholders = models.BigIntegerField(db_column='soldoutposHolders', blank=True, null=True)  # Field name made lowercase.
    buyersshares = models.BigIntegerField(db_column='buyersShares', blank=True, null=True)  # Field name made lowercase.
    buyers = models.BigIntegerField(blank=True, null=True)
    sellersshares = models.BigIntegerField(db_column='sellersShares', blank=True, null=True)  # Field name made lowercase.
    sellers = models.BigIntegerField(blank=True, null=True)
    nextyr = models.FloatField(blank=True, null=True)
    next5yr = models.FloatField(blank=True, null=True)
    meanrecthiswk = models.FloatField(blank=True, null=True)
    meanreclastwk = models.FloatField(blank=True, null=True)
    numbrokers = models.IntegerField(blank=True, null=True)
    shorts = models.FloatField(blank=True, null=True)
    shortsp = models.BigIntegerField(blank=True, null=True)
    shortsc = models.BigIntegerField(blank=True, null=True)
    shortsmove = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    rating = models.FloatField(db_column='RATING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sentiment'


class StocksPrice(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=1)
    date_ex = models.DateTimeField()
    open_p = models.DecimalField(max_digits=6, decimal_places=4)
    high_p = models.DecimalField(max_digits=6, decimal_places=4)
    low_p = models.DecimalField(max_digits=6, decimal_places=4)
    close_p = models.DecimalField(max_digits=6, decimal_places=4)
    volume = models.IntegerField()
    adj_close_p = models.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        db_table = 'stocks_price'


class StocksSentiment(models.Model):
    date_ex = models.DateTimeField()
    symbol = models.CharField(max_length=6)
    totalshares = models.IntegerField(db_column='totalShares')  # Field name made lowercase.
    totalholders = models.IntegerField(db_column='totalHolders')  # Field name made lowercase.
    newposshares = models.IntegerField(db_column='newposShares')  # Field name made lowercase.
    newposholders = models.IntegerField(db_column='newposHolders')  # Field name made lowercase.
    soldoutposshares = models.IntegerField(db_column='soldoutposShares')  # Field name made lowercase.
    soldoutposholders = models.IntegerField(db_column='soldoutposHolders')  # Field name made lowercase.
    buyersshares = models.IntegerField(db_column='buyersShares')  # Field name made lowercase.
    buyers = models.IntegerField()
    sellersshares = models.IntegerField(db_column='sellersShares')  # Field name made lowercase.
    sellers = models.IntegerField()
    nextyr = models.DecimalField(max_digits=6, decimal_places=2)
    next5yr = models.DecimalField(max_digits=6, decimal_places=2)
    meanrecthiswk = models.DecimalField(max_digits=3, decimal_places=2)
    meanreclastwk = models.DecimalField(max_digits=3, decimal_places=2)
    numbrokers = models.IntegerField()
    shorts = models.DecimalField(max_digits=3, decimal_places=2)
    shortsp = models.IntegerField()
    shortsc = models.IntegerField()
    shortsmove = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=8)
    company_name = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=12, decimal_places=10)

    class Meta:
        db_table = 'stocks_sentiment'


class StocksSymbol(models.Model):
    symbol = models.CharField(max_length=6)
    company = models.CharField(max_length=50)
    lastsale = models.DecimalField(max_digits=6, decimal_places=4)
    marketcap = models.IntegerField()
    adrtso = models.IntegerField()
    ipoyear = models.IntegerField()
    sector = models.CharField(max_length=20)
    industry = models.CharField(max_length=50)
    quotelink = models.CharField(max_length=50)

    class Meta:
        db_table = 'stocks_symbol'


class Symbol(models.Model):
    symbol = models.CharField(primary_key=True, max_length=10)
    company = models.CharField(max_length=255, blank=True, null=True)
    lastsale = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    marketcap = models.BigIntegerField(blank=True, null=True)
    adrtso = models.BigIntegerField(blank=True, null=True)
    ipoyear = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    sector = models.CharField(max_length=127, blank=True, null=True)
    industry = models.CharField(max_length=127, blank=True, null=True)
    quotelink = models.CharField(max_length=127, blank=True, null=True)

    def __str__(self):
    	return self.symbol
    	
    class Meta:
        db_table = 'symbol'
