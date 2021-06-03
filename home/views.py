from products.models import Product
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render



def home_page(request):
    product_suggestions = Product.objects.all().order_by('visited')[:6]
    return render(request,'home/home.html',{'product_suggestions': product_suggestions,})

    