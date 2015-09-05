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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80, primary_key=True)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


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
        unique_together = (('symbol', 'date_ex'),)


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
        unique_together = (('symbol', 'date_ex'),)


class StocksPrice(models.Model):
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

    class Meta:
        db_table = 'symbol'
