from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    
class Moves(models.Model):
    nome = models.CharField(max_length=100)
    precicao = models.IntegerField()
    poder = models.IntegerField()
    
      
def __str__(self):
    return self.name + "-" + self.tipo + "-" + self.peso + "-" + self.altura

