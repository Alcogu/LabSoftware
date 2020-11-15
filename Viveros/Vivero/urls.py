from django.urls import path
from Vivero import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('vivero/', views.vivero, name="Vivero"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)