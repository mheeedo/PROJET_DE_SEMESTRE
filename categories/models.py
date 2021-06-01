from django.db import models

class Categorie (models.Model):
    id_categorie = models.IntegerField(unique=True,primary_key=True)
    categorie_type = models.CharField(max_length=30)

    
