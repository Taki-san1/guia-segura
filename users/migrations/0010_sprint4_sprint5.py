"""
Migración 0010 - Sprint 4
Crea los modelos IntentoLogin, ScrapingLog, HistorialNotificacion
Compatible con el models.py del equipo (activo se mantiene en HistorialGuia)
"""
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_historialguia_activo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IntentoLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('intentos_fallidos', models.IntegerField(default=0)),
                ('bloqueado_hasta', models.DateTimeField(blank=True, null=True)),
                ('ultimo_intento', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_guia', models.CharField(max_length=200)),
                ('tipo_error', models.CharField(blank=True, max_length=120)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialNotificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_guia', models.CharField(max_length=200)),
                ('canal', models.CharField(max_length=50)),
                ('destinatario', models.CharField(blank=True, max_length=255)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('enviado', models.BooleanField(default=True)),
            ],
        ),
    ]