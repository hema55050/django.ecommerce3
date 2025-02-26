from django.db import models

# Create your models here.

class Product(models.Model):
   #image=""
   name = models.CharField(max_length=250)
   price = models.FloatField(default=0)
   alternatePrice = models.FloatField(default=0)
   rate = models.BigIntegerField()
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   def __str__(self):
      return self.name
from django.db import models


    