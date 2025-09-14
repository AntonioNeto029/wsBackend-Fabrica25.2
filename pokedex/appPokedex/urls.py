from django.urls import path, include
from . import views
from .views import listarPokemons, criarPokemons, buscarPokemons, deletarPokemon, atualizarPokemon

urlpatterns = [
    path('', views.home, name='home'),
    path('criarP/', criarPokemons, name='criarPokemons'),
    path('listarP/', listarPokemons, name='listarPokemons'),
    path('buscarP/', buscarPokemons, name='buscarPokemons'),
    path('deletarP/<int:pk>', deletarPokemon, name='deletarPokemon'),
    path('atualizarP/<int:pk>', atualizarPokemon, name='atualizarPokemon'),
]
