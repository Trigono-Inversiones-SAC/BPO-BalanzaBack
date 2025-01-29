from django.db import models


class Sede(models.Model):
    codigo = models.CharField(max_length=10, blank=True, null=True)
    distribucion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo}"


class Almacenes(models.Model):
    codigo = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo}"
    

class RegistroPeso(models.Model):
    TIPOS_CLIENTES = [('interno', 'Interno'), ('externo', 'Externo')]
    MOTIVOS = [('ingreso', 'Ingreso'), ('salida', 'Salida')]
    #general
    fecha = models.DateField(auto_now_add=True)
    tipo_cliente = models.CharField(max_length=50, choices=TIPOS_CLIENTES)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='registros_peso')
    empresa = models.CharField(max_length=255, blank=True, null=True)
    almacen = models.ForeignKey(Almacenes, on_delete=models.CASCADE, related_name='registros_peso')

    #gestión
    motivo = models.CharField(max_length=50, choices=MOTIVOS, blank=True, null=True)
    documento_tipo = models.CharField(max_length=255, blank=True, null=True)
    documento_numero = models.CharField(max_length=255, blank=True, null=True)
    doc_compra = models.CharField(max_length=255, blank=True, null=True)
    entidad_origen = models.CharField(max_length=255, blank=True, null=True)
    entidad_destino = models.CharField(max_length=255, blank=True, null=True)
    material = models.CharField(max_length=255, blank=True, null=True)
    lote = models.CharField(max_length=255, blank=True, null=True)
    conductor = models.CharField(max_length=255, blank=True, null=True)
    doc_identidad = models.CharField(max_length=255, blank=True, null=True)
    placa_camion = models.CharField(max_length=255, blank=True, null=True)
    placa_cisterna = models.CharField(max_length=255, blank=True, null=True)

    #pesos
    peso_remision = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)
    unidad_peso = models.CharField(max_length=20, blank=True, null=True)
    peso_bruto = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)
    peso_tara = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)
    peso_neto = models.DecimalField(max_digits=20, decimal_places=3, null=True, blank=True)

    #otros
    supervisor_origen = models.CharField(max_length=255, blank=True, null=True)
    supervisor_destino = models.CharField(max_length=255, blank=True, null=True)
    fecha_ingreso_balanza = models.DateField(auto_now_add=True)
    fecha_salida_balanza = models.DateField(blank=True, null=True)
    hora_ingreso_balanza = models.TimeField(auto_now_add=True)
    hora_salida_balanza = models.TimeField(blank=True, null=True)

    #observaciones
    observaciones = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Registro Peso {self.id} - {self.fecha}"
    

