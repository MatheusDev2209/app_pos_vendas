from django.db import models


# Create your models here.

#Comando para carregar informações no banco
#python .\manage.py makemigrations 

#depois executa o outro
#python .\manage.py migrate  

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.TextField(max_length=255)
    usuario = models.TextField(max_length=255)

class cliente (models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome_cli = models.TextField(max_length=255, blank=True, null=True)
    sobrenome = models.TextField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    wpp = models.TextField(max_length=255, blank=True, null=True)
    obs = models.TextField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.nome_cli


   
      