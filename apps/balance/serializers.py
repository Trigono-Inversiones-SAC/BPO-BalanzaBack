from rest_framework import serializers
from .models import *

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
        
class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacenes
        fields = '__all__'

class RegistroPesoSerializer(serializers.ModelSerializer):
    sede_codigo = serializers.ReadOnlyField(source='sede.codigo')
    almacen_name = serializers.ReadOnlyField(source='almacen.name')
    class Meta:
        model = RegistroPeso
        fields = '__all__'
