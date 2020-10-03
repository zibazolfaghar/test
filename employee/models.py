from django.db import models
from datetime import datetime


# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    salary = models.IntegerField()
    post = models.CharField(max_length=150)
    created_at = models.DateTimeField(null=True,blank=True)
    updated_at = models.DateTimeField(null=True,blank=True)

