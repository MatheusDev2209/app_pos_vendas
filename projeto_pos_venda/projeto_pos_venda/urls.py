
from django.contrib import admin
from django.urls import include, path
from app_cad_usuarios import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
   
    #sequencia correta
    # rota, views, nome de referenci
    path('usuarios/', views.usuarios, name='listagem_usuario'),
    path('usuarioregister/',views.cadastro, name='usuario'),
    path('admin/', admin.site.urls),
    path('index/', views.base, name='base'),
    path('dash/', views.dash, name='dash'),
    path('login/', views.login_view, name='login'),
    path('login/', views.logout_view, name='logout'),
    path('clientes/', views.clienteslista, name='clientes'),
    path('clientescadastro/', views.clientecadastro, name='clientecadastro'),
    
      #adicionar função de login
    
   
    #usuarios.com/usuarios
    
]
