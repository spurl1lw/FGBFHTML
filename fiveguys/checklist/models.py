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

class Accountmanager(models.Model):
    accmanagerid = models.ForeignKey('User', db_column='AccManagerID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'accountmanager'

class Administrator(models.Model):
    adminid = models.ForeignKey('User', db_column='AdminID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'administrator'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Checklist(models.Model):
    checklistid = models.IntegerField(db_column='ChecklistID', primary_key=True) # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'checklist'

class Checklistitem(models.Model):
    checklistid = models.ForeignKey(Checklist, db_column='ChecklistID') # Field name made lowercase.
    itemid = models.ForeignKey('Item', db_column='ItemID') # Field name made lowercase.
    checklistnotes = models.CharField(db_column='ChecklistNotes', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'checklistitem'

class Completedchecklists(models.Model):
    checklistid = models.ForeignKey(Checklist, db_column='ChecklistID') # Field name made lowercase.
    userid = models.ForeignKey('User', db_column='UserID') # Field name made lowercase.
    storeid = models.ForeignKey('Store', db_column='StoreID') # Field name made lowercase.
    checklistdate = models.DateField(db_column='ChecklistDate', blank=True, null=True) # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime', blank=True, null=True) # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'completedchecklists'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class Item(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True) # Field name made lowercase.
    templateid = models.ForeignKey('Template', db_column='TemplateID') # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'item'

class Manager(models.Model):
    managerid = models.ForeignKey('User', db_column='ManagerID', primary_key=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'manager'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

class Store(models.Model):
    storeid = models.CharField(db_column='StoreID', primary_key=True, max_length=3) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'store'

class Template(models.Model):
    templateid = models.IntegerField(db_column='TemplateID', primary_key=True) # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=20, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'template'

class User(models.Model):
    userid = models.CharField(db_column='UserID', primary_key=True, max_length=20) # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=15, blank=True) # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=15, blank=True) # Field name made lowercase.
    administrator = models.IntegerField(db_column='Administrator', blank=True, null=True) # Field name made lowercase.
    manager = models.IntegerField(db_column='Manager', blank=True, null=True) # Field name made lowercase.
    accountmanager = models.IntegerField(db_column='AccountManager', blank=True, null=True) # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=30, blank=True) # Field name made lowercase.
    autoemail = models.IntegerField(db_column='AutoEmail', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'user'

