import os
import time
import requests


def ejecutar_con_reintentos(funcion, intentos=3, espera_inicial=2, excepciones=(Exception,)):
    """Ejecuta una función con reintentos y backoff exponencial."""
    ultimo_error = None
    for intento in range(intentos):
        try:
            return funcion()
        except excepciones as error:
            ultimo_error = error
            if intento < intentos - 1:
                time.sleep(espera_inicial * (2 ** intento))
    raise ultimo_error


def enviar_estado_api_cliente(payload):
    """Envía el estado de una guía al API externo del cliente.

    Variables de entorno esperadas:
    CLIENT_API_URL: endpoint del cliente.
    CLIENT_API_TOKEN: token opcional Bearer.
    """
    url = os.getenv("CLIENT_API_URL", "").strip()
    token = os.getenv("CLIENT_API_TOKEN", "").strip()

    if not url:
        return {"success": False, "error": "CLIENT_API_URL no está configurada."}

    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    try:
        return response.json()
    except ValueError:
        return {"success": True, "status_code": response.status_code, "text": response.text}
