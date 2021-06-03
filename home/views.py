from products.models import Product
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render



def home_page(request):
    product_suggestions = Product.objects.all()
    return render(request,'home/home.html',{'product_suggestions': product_suggestions,})

    