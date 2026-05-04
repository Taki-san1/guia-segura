from django.contrib import admin
<<<<<<< HEAD
from .models import Perfil, HistorialGuia, LogNotificacion, LogScraping
=======
from .models import Perfil, HistorialGuia, IntentoLogin, ScrapingLog, HistorialNotificacion

>>>>>>> bdf1faca45c71a707fd893a0cbe68774fdfcf8c4

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')


@admin.register(HistorialGuia)
class HistorialGuiaAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'estado', 'fecha', 'hora', 'sucursal', 'fecha_consulta', 'usuario')
    list_filter = ('estado', 'sucursal', 'fecha_consulta')
    search_fields = ('numero_guia', 'usuario__username')

<<<<<<< HEAD
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
=======

@admin.register(IntentoLogin)
class IntentoLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'intentos_fallidos', 'bloqueado_hasta', 'ultimo_intento')
    search_fields = ('username', 'usuario__username')


@admin.register(ScrapingLog)
class ScrapingLogAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'tipo_error', 'fecha')
    search_fields = ('numero_guia', 'mensaje')
    list_filter = ('tipo_error', 'fecha')


@admin.register(HistorialNotificacion)
class HistorialNotificacionAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'canal', 'destinatario', 'fecha', 'enviado')
    search_fields = ('numero_guia', 'destinatario', 'mensaje')
    list_filter = ('canal', 'enviado', 'fecha')
>>>>>>> bdf1faca45c71a707fd893a0cbe68774fdfcf8c4
