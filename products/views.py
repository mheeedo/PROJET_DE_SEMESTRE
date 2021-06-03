from django.core.checks.messages import Info
from products.models import Product
import products
from django.shortcuts import render
from django.db.models import F

# Create your views here.


def update_count(myslug):
    Product.objects.filter(product_slug=myslug).update(visited=F('visited')+1)


def product_info(request,id_produit):
    update_count(id_produit)
    product_suggestions = Product.objects.all().order_by('visited')[:2]
    info = Product.objects.get(product_slug=id_produit)
    return render(request,'products/products.html',context={'Product': product_suggestions,'info': info,"data" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,1,1,1,1],})
