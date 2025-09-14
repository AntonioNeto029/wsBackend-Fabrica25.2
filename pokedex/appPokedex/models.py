from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField()
    peso = models.IntegerField()
    altura = models.IntegerField()
    # pokedexId = models.IntegerField()
    imagemUrl = models.URLField(blank=True, null=True)
    
# class Local(models.Model):
    
    
    
      
def __str__(self):
    return self.name

