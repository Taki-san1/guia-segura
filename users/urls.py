from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='users-home'),

    # Registro
    path('register/', views.VistaRegistro.as_view(), name='users-register'),

    # Perfil
    path('profile/', views.profile, name='users-profile'),

    # Lista de usuarios
    path('users-list/', views.VistaListaUsuarios.as_view(), name='users-list'),

    # Consulta de guía
    path('track-guide/', views.VistaConsultarGuia, name='track-guide'),

    # Login / Logout
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # --- PANEL USUARIOS PERSONALIZADO ---
    path('panel/usuarios/', views.panel_usuarios, name='panel_usuarios'),
    path('panel/usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('panel/usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('panel/usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('panel/usuarios/cambiar-rol/<int:user_id>/<str:rol>/', views.cambiar_rol_usuario, name='cambiar_rol_usuario'),
    # Usuarios inactivos / reactivación
    path('panel/usuarios/inactivos/', views.usuarios_inactivos, name='usuarios_inactivos'),
    path('panel/usuarios/activar/<int:user_id>/', views.activar_usuario, name='activar_usuario'),


    # ============================================================
    # 📦 CRUD DE HISTORIAL DE GUÍAS
    # ============================================================

    # Lista de consultas agrupadas por consulta_id
    path('panel/guias/', views.panel_guias, name='panel_guias'),

    path('panel/guias/reporte/', views.exportar_guias_excel, name='reporte_guias'),



    # Detalle de una consulta específica
    path('panel/guias/<int:consulta_id>/', views.detalle_consulta, name='detalle_consulta'),

    # Crear evento
    path('panel/guias/<int:consulta_id>/crear-evento/', views.crear_evento, name='crear_evento'),

    # Editar evento
    path('panel/guias/<int:consulta_id>/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),

    # Eliminar evento
    path('panel/guias/<int:consulta_id>/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),

    path('panel/guias/<int:consulta_id>/inactivos/', views.detalle_consulta_inactivos, name='detalle_consulta_inactivos'),
    path('panel/guias/<int:consulta_id>/restaurar/<int:evento_id>/', views.restaurar_evento, name='restaurar_evento'),

    #reporte excel

    path('panel/guias/exportar/', views.exportar_guias_excel, name='exportar_guias'),
    
]
