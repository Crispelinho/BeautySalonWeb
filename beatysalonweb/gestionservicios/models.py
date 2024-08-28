from django.db import models

# Create your models here.


class Servicio(models.Model):                            # se crea la tabla de Servicios
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    productosvarios = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return str(self.nombre)
    
#################################################################

# 
class TipoServicio(models.Model):                     # se crea la tabla de Tipos de Servicios
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'TipoServicio'
        verbose_name_plural = 'TiposServicios'

    def __str__(self):
        return str(self.nombre)
    
#########################################################