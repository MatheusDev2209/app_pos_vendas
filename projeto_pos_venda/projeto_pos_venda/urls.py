from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from app_cad_clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/',include('app_cad_clientes.urls')),
    path('dash/', views.dash, name='dash'),
     path('login/', views.login_view, name='login'),
    path('login/', views.logout_view, name='logout'),
]
