
from django.db.models.expressions import F

from products.models import Product
from django.shortcuts import render


def add_counter(id,slug):
    Product.objects.filter(id_product=id).update(times_visited=F('times_visited')+1)


def get_product_details(id,slug,request):
   product = Product.objects.filter(id_product=id)
   context = {'produit': product}
   return render(request, 'index.html', context)

        

    