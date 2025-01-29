from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .odoo.odoo_ordenes_compra import get_entidad_origen_y_material
from .serializers import *
from .models import *
from .services.DetectWeigth import BalanzaService

class DetailOrdenCompra(APIView):
    def get(self, request, orden_compra, *args, **kwargs):
        entidades_materiales = get_entidad_origen_y_material(orden_compra)
        return Response({'entidades_materiales': entidades_materiales}, status=status.HTTP_200_OK)

class SedeView(viewsets.ModelViewSet):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    
class AlmacenView(viewsets.ModelViewSet):
    serializer_class = AlmacenSerializer
    queryset = Almacenes.objects.all()

class RegistroPesoView(viewsets.ModelViewSet):
    serializer_class = RegistroPesoSerializer
    queryset = RegistroPeso.objects.all()
    
# ! Balanza Detect Weight View
balanza = BalanzaService()

class ListarPuertosView(APIView):
    def get(self, request):
        ports = balanza.listar_puertos()
        return Response({'ports': ports}, status=status.HTTP_200_OK)
    
class IniciarBalanzaView(APIView):
    def post(self, request, port_name):
        response = balanza.iniciar(port_name)
        return Response({'response': response}, status=status.HTTP_200_OK)
    
class DetenerBalanzaView(APIView):
    def post(self, request):
        response = balanza.detener()
        return Response({'response': response}, status=status.HTTP_200_OK)

class GetPesoView(APIView):
    def get(self, request):
        peso = balanza.peso_actual
        trama = balanza.trama_actual
        return Response({'peso': peso, 'trama':trama}, status=status.HTTP_200_OK)
    
