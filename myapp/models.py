from django.db import models
from datetime import datetime


# Create your models here.


class book(models.Model):
    Author = models.CharField(max_length=150)
    store_name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(default='', upload_to='store_image/', null=True, blank=True)
    fav = models.BooleanField(default=False)
    create_at = models.DateField(default=datetime.now)

    def str(self):
        return self.Author
