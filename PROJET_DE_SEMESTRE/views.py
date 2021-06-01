
from products.models import Product
from categories.models import Categorie
from django.shortcuts import redirect, render
from django.template import RequestContext

def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response



def category_products(request,id,slug):
  
    catdata = Categorie.objects.get(pk=id)
    products = Product.objects.filter(categorie=id) #default language
    
    context={'products': products,
             #'category':category,
             'catdata':catdata }
    return render(request,'detail_product.html',context)