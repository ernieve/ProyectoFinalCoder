from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('pais', 'estado', 'slug')
    list_filter = ('pais',)
    search_fields = ('pais',)

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('pais', 'destino', 'estado')
    list_filter = ('pais', 'destino')
    search_fields = ('pais', 'destino')

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo',)

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('avion', 'piloto', 'destino', 'fecha_salida', 'cupos', 'espacios_ocupados', 'estado', 'cupos_disponibles')