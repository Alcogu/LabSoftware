from django.urls import path
from Vivero import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #path('', login_required(views.inicio), name="Inicio"),
    path('', login_required(views.vivero), name="Vivero"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)