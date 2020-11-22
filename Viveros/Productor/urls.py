from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.productor, name="Productor"),
    path('listarproductor', views.productor_list, name ="listarproductor"),
    path('editarproductor/<int:id>/', views.editar_productor, name ="editarproductor"),
    path('eliminarproductor/<int:id>/', views.eliminar_productor, name ="eliminarproductor")
    #path('formularioProductor/', views.productor_view, name='FormularioProductor'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)