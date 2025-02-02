# Generated by Django 5.1.4 on 2025-01-22 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True)),
                ('distribucion', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroPeso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('tipo_cliente', models.CharField(choices=[('interno', 'Interno'), ('externo', 'Externo')], max_length=50)),
                ('empresa', models.CharField(blank=True, max_length=255, null=True)),
                ('almacen', models.CharField(choices=[('bravo 01', 'Bravo 01'), ('bravo 02', 'Bravo 02'), ('bravo 03', 'Bravo 03'), ('bravo 04', 'Bravo 04'), ('charly 01', 'Charly 01'), ('charly 02', 'Charly 02'), ('charly 03', 'Charly 03'), ('chancay 08', 'Chancay 08'), ('chancay exportacion', 'Chancay Exportación'), ('chancay virtual', 'Chancay Virtual'), ('chancay op.colombia', 'Chancay Op.Colombia'), ('bravo 05', 'Bravo 05'), ('charly 07', 'Charly 07')], max_length=50)),
                ('motivo', models.CharField(blank=True, choices=[('ingreso', 'Ingreso'), ('salida', 'Salida')], max_length=50, null=True)),
                ('documento_tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('documento_numero', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_compra', models.CharField(blank=True, max_length=255, null=True)),
                ('entidad_origen', models.CharField(blank=True, max_length=255, null=True)),
                ('entidad_destino', models.CharField(blank=True, max_length=255, null=True)),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('lote', models.CharField(blank=True, max_length=255, null=True)),
                ('conductor', models.CharField(blank=True, max_length=255, null=True)),
                ('doc_identidad', models.CharField(blank=True, max_length=255, null=True)),
                ('placa_camion', models.CharField(blank=True, max_length=255, null=True)),
                ('placa_cisterna', models.CharField(blank=True, max_length=255, null=True)),
                ('peso_remision', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('unidad_peso', models.CharField(blank=True, max_length=20, null=True)),
                ('peso_bruto', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('peso_tara', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('peso_neto', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True)),
                ('supervisor_origen', models.CharField(blank=True, max_length=255, null=True)),
                ('supervisor_destino', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_ingreso_balanza', models.DateField(auto_now_add=True)),
                ('fecha_salida_balanza', models.DateField(blank=True, null=True)),
                ('hora_ingreso_balanza', models.TimeField(auto_now_add=True)),
                ('hora_salida_balanza', models.TimeField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros_peso', to='balance.sede')),
            ],
        ),
    ]
