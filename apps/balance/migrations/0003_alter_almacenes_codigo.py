# Generated by Django 5.1.4 on 2025-01-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balance', '0002_almacenes_alter_registropeso_almacen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='almacenes',
            name='codigo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
