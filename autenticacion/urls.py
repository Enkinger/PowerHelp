from django.urls import path

from .views import URegistro, cerrar_sesion, logear

urlpatterns = [
    path('', URegistro.as_view(), name="autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    
]
