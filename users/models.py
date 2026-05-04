# users/models.py

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# =====================================================
# PERFIL DE USUARIO
# =====================================================
class Perfil(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='Mi biografía.', max_length=500, blank=True)

    # Seguridad: bloqueo por intentos fallidos
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado_hasta = models.DateTimeField(null=True, blank=True)

    def esta_bloqueado(self):
        from django.utils import timezone
        if self.bloqueado_hasta and timezone.now() < self.bloqueado_hasta:
            return True
        if self.bloqueado_hasta and timezone.now() >= self.bloqueado_hasta:
            # Auto-desbloqueo al expirar
            self.bloqueado_hasta = None
            self.intentos_fallidos = 0
            self.save(update_fields=['bloqueado_hasta', 'intentos_fallidos'])
        return False

    def registrar_intento_fallido(self):
        from django.utils import timezone
        from datetime import timedelta
        self.intentos_fallidos += 1
        if self.intentos_fallidos >= 5:
            self.bloqueado_hasta = timezone.now() + timedelta(minutes=15)
        self.save(update_fields=['intentos_fallidos', 'bloqueado_hasta'])

    def resetear_intentos(self):
        self.intentos_fallidos = 0
        self.bloqueado_hasta = None
        self.save(update_fields=['intentos_fallidos', 'bloqueado_hasta'])

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            img = Image.open(self.avatar.path)

            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.avatar.path)

        except FileNotFoundError:
            pass


# =====================================================
# HISTORIAL DE CONSULTAS DE GUÍAS
# =====================================================
class HistorialGuia(models.Model):
    consulta_id = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_guia = models.CharField(max_length=200)

    fecha = models.CharField(max_length=50, null=True, blank=True)
    hora = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    sucursal = models.CharField(max_length=255, null=True, blank=True)

    fecha_consulta = models.DateTimeField()



# =====================================================
# LOG DE ERRORES DE SCRAPING
# =====================================================
class LogScraping(models.Model):
    TIPO_ERROR = [
        ('timeout', 'Timeout'),
        ('guia_no_encontrada', 'Guía no encontrada'),
        ('dom_cambiado', 'DOM cambiado'),
        ('error_api', 'Error de API'),
        ('otro', 'Otro'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    numero_guia = models.CharField(max_length=200)
    tipo_error = models.CharField(max_length=30, choices=TIPO_ERROR, default='otro')
    mensaje = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return f"[{self.tipo_error}] {self.numero_guia} – {self.creado_en:%d/%m/%Y %H:%M}"
# =====================================================
class LogNotificacion(models.Model):
    CANAL_CHOICES = [
        ('email', 'Email'),
        ('sistema', 'Sistema'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    numero_guia = models.CharField(max_length=200)
    canal = models.CharField(max_length=20, choices=CANAL_CHOICES, default='email')
    mensaje = models.TextField()
    enviado_en = models.DateTimeField(auto_now_add=True)
    exitoso = models.BooleanField(default=True)

    class Meta:
        ordering = ['-enviado_en']

    def __str__(self):
        return f"{self.canal} → {self.usuario.username} [{self.numero_guia}] {self.enviado_en:%d/%m/%Y %H:%M}"