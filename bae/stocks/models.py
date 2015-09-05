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
    symbol = models.CharField(max_length=10, primary_key=True)
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
    symbol = models.CharField(max_length=10, primary_key=True)
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
