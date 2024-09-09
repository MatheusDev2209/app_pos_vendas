from app_cad_clientes import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    #sequencia correta
    # rota, views, nome de referenci
    path('usuarios/', views.usuarios, name='listagem_usuario'),
    path('usuarioregister/',views.cadastro, name='usuario'),
    
    
    path('login/', views.login_view, name='login'),
    path('login/', views.logout_view, name='logout'),
    path('clientes/', views.clienteslista, name='clientes'),
    path('clientescadastro/', views.clientecadastro, name='clientecadastro'),
]