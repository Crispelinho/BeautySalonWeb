from django.db import models

from beatysalonweb.negocios.models import AreaNegocio

# Create your models here.

class Factura(models.Model):                               # se crea la tabla de Fctura
    id = models.AutoField(primary_key= True)
    referencia = models.CharField(max_length=50)           # que tipo de referencia son ? Texto o Numericas ?
    fechayhora = models.DateTimeField(auto_now_add= True)
    total = models.IntegerField()
    intemfacturavarios = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return str(self.nombre)

#################################################################


class ItemFactura(models.Model):                               # se crea la tabla de Item de Factura
    id = models.AutoField(primary_key= True)
    factura = models.CharField(max_length=50)                # que tipo de variable es la factura ? Texto o Numericas ?
    serviciovarios = models.CharField(max_length=100)
    productovarios = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'ItemFactura'
        verbose_name_plural = 'ItemFacturas'

    def __str__(self):
        return str(self.nombre)

#################################################################


class Ordendecompra(models.Model):                               # se crea la tabla de Fctura
    id = models.AutoField(primary_key= True)
    referencia = models.CharField(max_length=50)           # que tipo de variable es referencia ? Texto o Numericas ?
    fechayhora = models.DateTimeField(auto_now_add= True)
    total = models.IntegerField()
    proveedor = models.CharField(max_length=100)
    productovarios = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Ordendecompra'
        verbose_name_plural = 'Ordendecompras'

    def __str__(self):
        return str(self.nombre)

#################################################################


class Producto(models.Model):                               # se crea la tabla de Fctura
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=50)           # que tipo de referencia son ? Texto o Numericas ?
    precio = models.IntegerField()
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.nombre)

#################################################################

class Proveedor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    correo = models.EmailField()
    area_negocio = models.ForeignKey(AreaNegocio, on_delete=models.CASCADE)     

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return str(self.nombre)