from django.contrib import admin
from .models import Equipos, Trabajos

# Register your models here.
@admin.register(Equipos)
class EquiposAdmin(admin.ModelAdmin):
    pass

@admin.register(Trabajos)
class TrabajosAdmin(admin.ModelAdmin):
    pass 