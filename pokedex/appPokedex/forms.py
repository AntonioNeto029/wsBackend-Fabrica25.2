from django import forms
from .models import Pokemon, Moves

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ["nome", "tipo", "peso", "altura"]
        
class MoveForm(forms.ModelForm):
    class Meta:
        model = Moves
        fields = ["nome"]
        