from django.contrib import admin

# Register your models here.

from .models import Marketplace, Product

admin.site.register(Marketplace)
admin.site.register(Product)  
