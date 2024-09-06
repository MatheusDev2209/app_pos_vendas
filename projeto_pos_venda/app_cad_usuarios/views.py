
from django.shortcuts import  render, redirect
from .models import Usuarios, cliente
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm
from django.contrib import messages
####################################################### VIEWS DA BASE #######################################################
@login_required
def base (request):
    return render(request, 'usuarios/base.html')

####################################################### VIEWS DE LOGIN E LOGOUT #######################################################
def login_view(request):
#Login do usuario autenticando usuarios criados no admin    
    error_msg = ""
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dash')  # Redirecione para a página inicial ou outra página
        else:
            error_msg = "Senha ou Usuario Incorretos"
    else:
        form = CustomLoginForm()
    return render(request, 'usuarios/login.html', {'form': form, 'error_msg': error_msg})
    
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecione para a página de login ou outra página

# Função para chamar a tela de cadastro de usuarios
def usuariologin(request):
    return render(request, 'usuarios/login.html')
####################################################### FIM VIEWS DE LOGIN #######################################################

####################################################### VIEWS DE CLIENTE #######################################################
def clienteslista(request):
    pessoas = cliente.objects.all()
    return render(request, 'usuarios/listar_clientes.html', {'pessoas': pessoas})

#def clientecadastro(request):
#    if request.method == 'POST':
#        form = clientes(request.POST)
#        if form.is_valid():
#            task = form.save()
        
#            print("sucesso")
#            return redirect('usuarios/listar_clientes.html')  # Redirecione para a página inicial ou outra página
#    else:    

 #       form = clientes
#        return render(request, 'usuarios/clientes.html', {'form': form})
def clientecadastro(request):
    if request.method == 'POST':
        novo_cliente = cliente()
        novo_cliente.nome_cli = request.POST.get('nome')
        novo_cliente.sobrenome = request.POST.get('sobrenome')
        novo_cliente.email = request.POST.get('email')
        novo_cliente.wpp = request.POST.get('wpp')
        novo_cliente.obs = request.POST.get('obs')
        novo_cliente.save()
        messages.success(request, "Cliente cadastrado com sucesso!")
        # Exibir todos os usuarios ja cadastrado em uma nova pagina
        pessoas = {
        'pessoas' : cliente.objects.all
        }
    # Retornar os dados para a página de listagem
        return render(request, 'usuarios/listar_clientes.html', pessoas)
    else:    

        return render(request, 'usuarios/clientes.html')
    


####################################################### FIM VIEWS DE CLIENTE #######################################################

####################################################### VIEWS DA DASH #######################################################
def dash(request):
    return render(request, 'usuarios/dash.html')

####################################################### VIEWS CADASTRO USUARIO #######################################################
def cadastro(request):
  return render(request, 'usuarios/cadastro.html')


def usuarios(request):
    # SALVAR OS DADOS DA TELA PARA O BANCO DE DADOS
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.sobrenome = request.POST.get('sobrenome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.usuario = request.POST.get('usuario')
    novo_usuario.save()
    
    # Exibir todos os usuarios ja cadastrado em uma nova pagina
    usuarios = {
        'usuarios' : Usuarios.objects.all
    }

    # Retornar os dados para a página de listagem

    return render(request, 'usuarios/listar.html', usuarios)
####################################################### FIM VIEWS DE USUARIO #######################################################




