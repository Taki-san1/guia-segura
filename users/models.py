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
    activo = models.BooleanField(default=True)   # 🔥 NUEVO

    
    
