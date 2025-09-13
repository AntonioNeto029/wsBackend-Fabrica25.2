from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Pokemon, Moves
from .forms import PokemonForm, MoveForm

import requests 


def home(request):
    return render(request, 'home.html')


def listarPokemons(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'listPokemon.html', {'pokemons': pokemons})

def criarPokemons(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarPokemons')
    else:
        form = PokemonForm()
    return render(request, 'createPokemon.html', {'pokemon': form})

def deletarPokemon(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('listarPokemons')
    return render(request, 'confirmarDelete.html', {'pokemon': pokemon})

def atualizarPokemon(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('listarPokemons')
    else:
        form = PokemonForm(instance=pokemon)
        return render(request, 'createPokemon.html', {'pokemon': form})
     
     
     
     
# def buscarPokemons(request):
#     response = requests.get('https://pokeapi.co/api/v2/pokemon/{pokemonNome}/')
#     dadosPokemon = response.json()
#     pokemon = Pokemon.objects.create(
#         nome = dadosPokemon["name"],
#         altura = dadosPokemon["height"],
#         peso = dadosPokemon["weight"],
#         tipo = dadosPokemon["types"]
#     )
    
#     return HttpResponse(dadosPokemon["name", "height", "weight", "types"])       

# appPokedex/views.py

def buscarPokemons(request):
    pokemonNome = request.GET.get('nome', '').lower()
    context = {}

    if not pokemonNome:
        context['error'] = "Por favor, digite o nome de um Pokémon."
        return render(request, 'pokemon_detail.html', context)

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemonNome}/"
    response = requests.get(url)

    if response.status_code == 200:
        dadosPokemon = response.json()

        pokemon_data = {
            'nome': dadosPokemon['name'],
            'id': dadosPokemon['id'],
            'altura': dadosPokemon['height'] / 10.0,
            'peso': dadosPokemon['weight'] / 10.0,
            'sprite_url': dadosPokemon['sprites']['front_default'],
            'tipos': [tipo['type']['name'] for tipo in dadosPokemon['types']],
            'habilidades': [h['ability']['name'] for h in dadosPokemon['abilities']]
        }
        context['pokemon'] = pokemon_data
    else:
        context['error'] = f"Pokémon '{pokemonNome}' não encontrado. Tente novamente."

    return render(request, 'pokedex.html', context)