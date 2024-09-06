# meu_app/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário', max_length=63,  widget=forms.TextInput(
            attrs={
                'class': 'form-control col-md-2 form-control-lg',
                'placeholder': 'Ex.: João Silva',
            }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
                'class': 'form-control col-md-2 form-control-lg',
                'placeholder': 'Senha',
            }))


#class clientes(forms.Form):
    
#    model = cliente
#    nome = forms.CharField(label='Nome', max_length=20, widget=forms.TextInput(
#            attrs={
#                'class': 'form-control',
 #               'placeholder': 'Ex.: João',
#            }))
#    sobrenome = forms.CharField(label='Sobrenome', max_length=20, widget=forms.TextInput(
#            attrs={
#                'class': 'form-control',
#                'placeholder': 'Ex.:Silva',
#            }))
#    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(
#            attrs={
#                'class': 'form-control',
#                'placeholder': 'example@email.com',
#            }))
#    wpp = forms.CharField(label='wpp', max_length=15, widget=forms.TextInput(
#            attrs={
#                'class': 'form-control',
#                'placeholder': '+55 88 999993333',
#            }))
#    obs = forms.CharField(label='obs', max_length=100, widget=forms.TextInput(
#            attrs={
#                'class': 'form-control',
#                'placeholder': 'Digite uma mensagem adicional (opcional)',
#            }))