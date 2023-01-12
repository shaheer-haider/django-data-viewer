from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name