from django.contrib import admin
from django.urls import path
from Vivero import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
#Importamos librerias para el Login
from django.contrib.auth import login, logout
from Login.views import Login, logoutUsuario  
from django.contrib.auth.decorators import login_required
from .views import inicio
from Login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('Usuario.urls', 'usuario'))),
    path('', login_required(inicio), name = 'Inicio'),
    path('vivero/', include(('Vivero.urls', 'vivero'))),
    path('productor/', include('Productor.urls')),
    path('labor/', include('Labor.urls')),
    path('accounts/login/', Login.as_view(), name = 'login'),
    path('logout/', login_required(logoutUsuario), name = 'logout' ),
    #path('iniciosesion/', include('Login.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()
