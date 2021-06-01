from authentication.models import Account
from products.models import Product
from django.db import models
from authentication.models import Account

class orders(models.Model):
    product = models.ForeignKey(Product)
    canceled = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(Account)
    quantity = models.IntegerField(blank=False,null=False)
    
