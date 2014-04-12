# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group


class Checklist(models.Model):
    type = models.CharField(db_column='Type', max_length=20, blank=True) # Field name made lowercase.


class Checklistitem(models.Model):
    checklistid = models.ForeignKey(Checklist) # Field name made lowercase.
    itemid = models.ForeignKey('Item') # Field name made lowercase.
    checklistnotes = models.CharField(max_length=200, blank=True, null=True) # Field name made lowercase.


class Completedchecklists(models.Model):
    checklistid = models.ForeignKey(Checklist) # Field name made lowercase.
    userid = models.ForeignKey(User) # Field name made lowercase.
    storeid = models.ForeignKey('Store') # Field name made lowercase.
    checklistdate = models.DateField( blank=True, null=True) # Field name made lowercase.
    starttime = models.TimeField(blank=True, null=True) # Field name made lowercase.
    endtime = models.TimeField( blank=True, null=True) # Field name made lowercase.


class Item(models.Model):

    templateid = models.ForeignKey('Template') # Field name made lowercase.
    description = models.CharField(max_length=200, blank=True, null=True) # Field name made lowercase.


class Store(models.Model):
    storeid = models.CharField(primary_key=True, max_length=3, unique=True) # Field name made lowercase.


class Template(models.Model):
    templatename = models.CharField(max_length=20, blank=True) # Field name made lowercase.


class Managers(models.Model):

    user = models.OneToOneField(User)

    is_manager = models.BooleanField("Is Manager",default=False)
    is_account_manger = models.BooleanField("Is Account Manager",default=False)
    auto_email  = models.BooleanField("Auto EMail Reports",default=False)
