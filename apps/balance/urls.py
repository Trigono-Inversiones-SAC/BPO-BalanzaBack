from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'registros_pesos', RegistroPesoView, basename='registros_pesos')
router.register(r'sedes', SedeView, basename='sedes')
router.register(r'almacenes', AlmacenView, basename='almacenes')


urlpatterns = [
    path('entidades_materiales/<str:orden_compra>/', DetailOrdenCompra.as_view(), name='entidades_materiales'),
    
    # ! Balanza Detect Weight URL 
    path('detect_weight/puertos/', ListarPuertosView.as_view(), name='listar-puertos'),
    path('detect_weight/iniciar/<str:port_name>/', IniciarBalanzaView.as_view(), name='iniciar'),
    path('detect_weight/detener/', DetenerBalanzaView.as_view(), name='detener'),
    path('detect_weight/', GetPesoView.as_view(), name='get-peso'),
    
] + router.urls