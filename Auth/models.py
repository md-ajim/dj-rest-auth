from django.db import models

class MyModel(models.Model):
    id = models.IntegerField(primary_key=True)  # or use models.CharField(max_length=... ) if IDs are non-integer
    name = models.CharField(max_length=100)




class MyModels(models.Model):
    id = models.IntegerField(primary_key=True)  # or use models.CharField(max_length=... ) if IDs are non-integer
    name = models.CharField(max_length=100)
