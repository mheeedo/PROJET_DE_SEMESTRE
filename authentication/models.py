



from django.contrib.auth.models import AbstractBaseUser
from django.db import models
gender_choices =[
  ('M','male'),
  ('F','female'),
]
class Account(AbstractBaseUser):
   
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    gender = models.CharField(max_length=10,choices=gender_choices)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.IntegerField()
    adresse = models.CharField(max_length=100,blank = False)
    ville = models.CharField(max_length=20)
    pays = models.CharField(max_length=100)

    


    def get_email(self):
       return self.email
    
    def join_first_last(self):
        return ' '.join([self.first_name, self.last_name])

    def __unicode__(self) :
        return self.username

    def get_password(self):
        return self.password