from products.models import Product
from django.db import models
from authentication.models import Account
class Cart(models.Model):
    id_order = models.IntegerField(unique=True,primary_key=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    canceled = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(Account,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False,null=False)