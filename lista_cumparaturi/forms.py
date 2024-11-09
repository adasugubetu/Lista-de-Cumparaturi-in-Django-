from django import forms
from .models import Produs

class ProdusForm(forms.ModelForm):
    class Meta:
        model = Produs
        fields = ['nume']
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume produs'}),
        }
