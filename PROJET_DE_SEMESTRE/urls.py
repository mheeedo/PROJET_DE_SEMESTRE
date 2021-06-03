"""PROJET_DE_SEMESTRE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views as views_home
from django.conf import settings
from django.conf.urls.static import static
from products import views as views_products


urlpatterns = [
    path('',views_home.home_page),
    path('admin/', admin.site.urls),
    path('authentication/',include('authentication.urls')),
    path('home/',views_home.home_page,name='home'),
    path('products/id_product=<slug:id_produit>',views_products.product_info,name='products')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



