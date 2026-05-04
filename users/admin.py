from django.contrib import admin
from .models import Perfil, HistorialGuia, LogNotificacion, LogScraping

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')

@admin.register(HistorialGuia)
class HistorialGuiaAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'estado', 'fecha', 'hora', 'sucursal', 'fecha_consulta', 'usuario')
    list_filter = ('estado', 'sucursal', 'fecha_consulta')
    search_fields = ('numero_guia', 'usuario__username')

@admin.register(LogNotificacion)
class LogNotificacionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'numero_guia', 'canal', 'enviado_en', 'exitoso')
    list_filter = ('canal', 'exitoso', 'enviado_en')
    search_fields = ('usuario__username', 'numero_guia')

@admin.register(LogScraping)
class LogScrapingAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'tipo_error', 'usuario', 'creado_en')
    list_filter = ('tipo_error', 'creado_en')
    search_fields = ('numero_guia', 'mensaje')