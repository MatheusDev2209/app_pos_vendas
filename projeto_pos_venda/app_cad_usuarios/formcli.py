from django import forms
from .models import cliente

class PessoaForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nome', 'sobrenome', 'email', 'wpp', 'obs']