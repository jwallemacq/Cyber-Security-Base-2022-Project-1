from django.db import models
from django.contrib.auth.models import User

class Marketplace(models.Model):
    marketplace_text = models.CharField(max_length=50)
    def __str__(self):
        return self.marketplace_text

class Product(models.Model):
    supplier = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product_text = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    def __str__(self):
        return self.product_text
    
