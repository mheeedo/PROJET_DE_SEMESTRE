from django.db import models

class Categorie (models.Model):
    categorie_type = models.CharField(max_length=30)

    
