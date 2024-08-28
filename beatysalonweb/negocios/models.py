from django.db import models

# Create your models here.
class AreaNegocio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'AreaNegocio'
        verbose_name_plural = 'AreasNegocios'

    def __str__(self):
        return str(self.nombre)

class Negocio(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=40)
    razon_social = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    nit = models.IntegerField()
    correo = models.EmailField()
    area_negocio = models.ForeignKey(AreaNegocio, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Negocio'
        verbose_name_plural = 'Negocios'

    def __str__(self):
        return str(self.nombre)
    