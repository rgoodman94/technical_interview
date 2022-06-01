from django.db import models


# Create your models here.
class CatRecords(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField
    birth_date = models.DateTimeField(db_column='birthDate')
