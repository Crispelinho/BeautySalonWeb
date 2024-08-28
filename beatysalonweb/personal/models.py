from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    telefono = models.ImageField()
    redsocial1 = models.CharField(max_length=100)
    redsocial2 = models.CharField(max_length=100)
    redsocial3 = models.CharField(max_length=100)
    direccion = models.CharField(max_length=40)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return str(self.nombre)

######################################################################
   
class Empleado(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=50)
    telefono = models.ImageField()
    redsocial1 = models.CharField(max_length=100)
    redsocial2 = models.CharField(max_length=100)
    redsocial3 = models.CharField(max_length=100)
    direccion = models.CharField(max_length=40)
          
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return str(self.nombre)
                                    