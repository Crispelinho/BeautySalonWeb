from django.contrib import admin
from negocios.models import Negocio, AreaNegocio

# Register your models here.

class AreaNegocioAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "descripcion",)
    list_filter = ("nombre",)
    
class NegocioAdmin(admin.ModelAdmin):
    list_display = ("id","nombre", "razon_social", "direccion", "nit", "correo", "area_negocio__nombre")
    list_filter = ("razon_social",)
    
admin.site.register(Negocio, NegocioAdmin)
admin.site.register(AreaNegocio, AreaNegocioAdmin)