from django.contrib import admin
from .models import Equipos, Trabajos

# Register your models here.
class EquiposAdmin(admin.ModelAdmin):
    list_display = ('id_equipo','serial', 'descripcion', 'marca', 'modelo', 'activonuevo', 'activoviejo','responsable', 'cargo','ubicacion')
    search_field = ('id_equipo', 'serial', 'activoviejo', 'activonuevo', 'responsable', 'ubicacion')

admin.site.register(Equipos, EquiposAdmin)

class TrabajosAdmin(admin.ModelAdmin):
    list_display = ('id_trabajos', 'nombre', 'fechainicio', 'fechafin')
    search_fields = ('id_trabajos','id_equipos', 'nombre', 'fechainicio', 'fechafin',)

admin.site.register(Trabajos, TrabajosAdmin)