from django.db import models

# Create your models here.

class Notes(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_collation='utf8mb4_bin')
    ownerid = models.ForeignKey('Users', models.DO_NOTHING, db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    shortid = models.CharField(max_length=255)
    permission = models.CharField(max_length=9, blank=True, null=True)
    viewcount = models.IntegerField(blank=True, null=True)
    lastchangeuserid = models.CharField(db_column='lastchangeuserId', max_length=36, db_collation='utf8mb4_bin', blank=True, null=True)  # Field name made lowercase.
    lastchangeat = models.DateTimeField(db_column='lastchangeAt', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(max_length=255, blank=True, null=True)
    savedat = models.DateTimeField(db_column='savedAt', blank=True, null=True)  # Field name made lowercase.
    authorship = models.TextField(blank=True, null=True)
    deletedat = models.DateTimeField(db_column='deletedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Notes'
  
