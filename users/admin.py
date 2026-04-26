from django.contrib import admin
from .models import Perfil, HistorialGuia

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')

@admin.register(HistorialGuia)
class HistorialGuiaAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'estado', 'fecha', 'hora', 'sucursal', 'fecha_consulta', 'usuario')
    list_filter = ('estado', 'sucursal', 'fecha_consulta')
    search_fields = ('numero_guia', 'usuario__username')
