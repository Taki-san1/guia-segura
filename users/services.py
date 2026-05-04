"""
users/services.py
Funciones auxiliares para el scraping y la integración con APIs externas.
"""
import time
import requests


def ejecutar_con_reintentos(func, intentos=3, espera_inicial=2):
    """
    Ejecuta una función con reintentos automáticos en caso de error.
    Usa backoff exponencial entre intentos.
    """
    ultimo_error = None
    for intento in range(intentos):
        try:
            return func()
        except Exception as e:
            ultimo_error = e
            if intento < intentos - 1:
                time.sleep(espera_inicial * (2 ** intento))
    raise ultimo_error


def enviar_estado_api_cliente(payload):
    """
    Envía el estado de una guía a la API del cliente si está configurada.
    Si no hay URL configurada, retorna success=True sin hacer nada.
    """
    import os
    api_url = os.getenv("API_CLIENTE_URL", "").strip()

    if not api_url:
        return {"success": True, "mensaje": "API cliente no configurada"}

    try:
        r = requests.post(api_url, json=payload, timeout=10)
        return {"success": r.status_code < 400, "status": r.status_code}
    except Exception as e:
        return {"success": False, "error": str(e)}