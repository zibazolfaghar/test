from django.db import models
from datetime import datetime


# Create your models here.


class students(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=50)
    stnum = models.IntegerField()
    TEACHER=(("ali","ali"),
             ("sara","sara"),
             ("sima","sima")

             )
    teacher=models.CharField(max_length=50,choices=TEACHER)



