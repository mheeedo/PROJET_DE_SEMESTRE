

from django.urls import path
from django.urls.conf import re_path

from . import views

urlpatterns = [
  path('test/',views.about)
  
]

""" les urls li ghadi ta7tage
login
logout
register 
profile (doit etre connecter sinon non disponible)


"""