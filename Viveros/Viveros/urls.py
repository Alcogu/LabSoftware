from django.contrib import admin

from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]

from Vivero import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from Vivero import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Vivero.urls')),
    path('productor/', include('Productor.urls')),
    path('labor/', include('Labor.urls')),
    path('iniciosesion/', include('Login.urls'))

]

urlpatterns += staticfiles_urlpatterns()