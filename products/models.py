from django.db import models
from django.db.models.expressions import OrderBy

class Product(models.Model):
    product_slug = models.SlugField(unique=True,blank=False)
    name = models.CharField(max_length=100,blank=False,null=False)
    thumbnail = models.ImageField(upload_to='product_pics')
    """ a verifier"""
    description = models.TextField()
    available = models.BooleanField(default=True)
    price = models.IntegerField()
    discount = models.IntegerField(default=100)
    visited= models.IntegerField(default=0)
    added = models.DateTimeField(auto_now_add=True)

 




    


    
