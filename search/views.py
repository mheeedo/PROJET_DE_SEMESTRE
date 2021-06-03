from django.shortcuts import render
from products import models



def search(request):

    if request.method == "POST":
        searched = request.POST.get('searched')

        if  searched :
            product = models.Product.objects.filter(name__contains=searched)
            return render(request,'search/search.html',{'searched' : searched,'products':product})
        else:
            return render(request,'search/search.html',{'searched' : searched,})
    else:
        return render(request,'search/search.html',{})
