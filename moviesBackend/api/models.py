from django.db import models

# Create your models here.
class Movies(models.Model):

    title= models.CharField(max_length=400)
    photo= models.CharField(max_length=400)
    year= models.CharField(max_length=400)
    vedio= models.CharField(max_length=400)
    actors= models.CharField(max_length=400)
    director= models.CharField(max_length=400)
    rate= models.CharField(max_length=400)
