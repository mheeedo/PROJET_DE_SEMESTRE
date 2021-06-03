

from django.urls import path
from django.urls.conf import re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('login/',auth_views.LoginView.as_view(template_name='authentication/login.html'),name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name='authentication/logout.html'),name='logout'),
  path('register/',views.register,name='register'),
  path('profile/id_user=<slug:id_profile>',views.profile,name='profile'),
  
]

