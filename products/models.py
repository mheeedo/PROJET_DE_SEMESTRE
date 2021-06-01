
from categories.models import Categorie
from django.db import models


size_choices =[
    ('ES','extra small'),
    ('S','small'),
    ('M','medium'),
    ('L','large'),
    ('XL','extra large'),
]


class Product(models.Model):
    slug = models.SlugField(blank=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(blank=False,null=False)
    price = models.DecimalField(blank=False,null=False,decimal_places=3,max_digits=9)
    sizes = models.CharField(max_length=100,blank=False)
    times_visited = models.IntegerField(default=0)
    class meta:
         ordering = ('times_visited',)



class Image_album(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images')

class product_sizes(models.Model):
     product = models.ForeignKey(Product,on_delete=models.CASCADE)
     sizes = models.CharField(choices=size_choices,blank=False,null=False,max_length=100)


    
