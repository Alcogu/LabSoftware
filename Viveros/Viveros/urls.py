"""Viveros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#<<<<<<< HEAD
from django.urls import path
#<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
]
#=======
from Vivero import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#=======
from django.urls import path, include
from Vivero import views 

#>>>>>>> dimas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vivero.urls')),
    path('productor/', include('Productor.urls')),
    #path('formularioProductor/', include('Productor.urls')),
    path('labor/', include('Labor.urls')),
    path('iniciosesion/', include('Login.urls'))

]

#<<<<<<< HEAD
urlpatterns += staticfiles_urlpatterns()
#>>>>>>> dimas
#=======
#>>>>>>> dimas
