from django.db import models

class Pokemon(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    peso = models.IntegerField()
    altura = models.IntegerField()
    imagemUrl = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.nome
    
class Treinador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
      
    def __str__(self):
        return self.nome

