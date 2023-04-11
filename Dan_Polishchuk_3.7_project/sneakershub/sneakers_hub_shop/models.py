import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')

class Orders(models.Model):
    Model = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)
    Size = models.CharField(max_length=255)
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)


admin.site.register(Product, ProductAdmin)