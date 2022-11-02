from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateField(db_column='DATE', primary_key=True)  # Field name made lowercase.
    data = models.BigIntegerField(db_column='DATA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'


class Data20002021(models.Model):
    date = models.DateField(db_column='DATE', primary_key=True)  # Field name made lowercase.
    data = models.BigIntegerField(db_column='DATA')  # Field name made lowercase.
    data2 = models.BigIntegerField(db_column='DATA2')  # Field name made lowercase.
    data3 = models.BigIntegerField(db_column='DATA3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data(2000-2021)'


class Data20072021(models.Model):
    date = models.DateField(db_column='DATE', primary_key=True)  # Field name made lowercase.
    data = models.BigIntegerField(db_column='DATA')  # Field name made lowercase.
    data2 = models.BigIntegerField(db_column='DATA2')  # Field name made lowercase.
    data3 = models.BigIntegerField(db_column='DATA3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data(2007-2021)'


class Post(models.Model):

  title = models.CharField(max_length=50)

  text = models.TextField()

 

  def __str__(self):

  	return self.title