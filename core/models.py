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
    
class Payments(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    expiration_date = models.CharField(max_length=255)
    cvv = models.CharField(max_length=255)
    amount = models.IntegerField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
    

class Currency(models.Model):
    name = models.CharField(max_length=255)
    value_per_bitcoin = models.FloatField()
    
    def __str__(self):
        return self.name
    
    
class CurrencyHistory(models.Model):
    date = models.DateField()
    rate = models.FloatField()
    coin = models.CharField(max_length=255, default="BTC")
    target_currency = models.CharField(max_length=255, default="USD")
    
    def __str__(self):
        return self.coin + " to " + self.target_currency + " on " + str(self.date)


class DynamicJson(models.Model):
    name = models.CharField(max_length=255)
    json = models.JSONField()
    
    def __str__(self):
        return self.name