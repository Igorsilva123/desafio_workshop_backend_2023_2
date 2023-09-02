from django.db import models


# Create your models here.

class Marcas(models.Model):
    nome = models.CharField(max_length=20)
    localizacao = models.CharField(max_length=20)
    

class Carros(models.Model):
    nome = models.CharField(max_length=20)
    preco = models.IntegerField()
    marca_id = models.IntegerField()
    ano = models.IntegerField()
    
