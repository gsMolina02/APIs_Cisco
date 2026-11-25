"""Cliente mínimo de la API REST de Webex usado por los scripts del laboratorio 8.6.7 (GR08).

Los datos privados no se escriben en el código:
  - El token se toma de la variable de entorno WEBEX_TOKEN o de config.json (clave "access_token").
  - Correo del compañero, título de la sala, ID de la sala y mensaje se leen de config.json.
config.json está en .gitignore: copie config.example.json como config.json y complételo.
"""
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit('Falta la librería requests. Instálela con:  pip install -r requirements.txt')

API = 'https://webexapis.com/v1'
CARPETA = Path(__file__).resolve().parent
CONFIG = CARPETA / 'config.json'


def config(*obligatorias):
    """Lee config.json y comprueba que las claves pedidas tengan un valor real."""
    datos = {}
    if CONFIG.exists():
        with open(CONFIG, encoding='utf-8') as archivo:
            datos = json.load(archivo)
    if os.environ.get('WEBEX_TOKEN'):
        datos['access_token'] = os.environ['WEBEX_TOKEN']
    for clave in ('access_token',) + obligatorias:
        valor = str(datos.get(clave, '')).strip()
        if not valor or valor.startswith('<'):
            sys.exit(f'Falta "{clave}" en config.json (copie config.example.json como config.json).')
    return datos


def guardar(clave, valor):
    """Guarda un valor en config.json; se usa para recordar el ID de la sala creada."""
    datos = {}
    if CONFIG.exists():
        with open(CONFIG, encoding='utf-8') as archivo:
            datos = json.load(archivo)
    datos[clave] = valor
    with open(CONFIG, 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def encabezados(token):
    return {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}


def get(recurso, token, **parametros):
    return _enviar('GET', recurso, token, params=parametros)


def post(recurso, token, cuerpo):
    return _enviar('POST', recurso, token, json=cuerpo)


def _enviar(metodo, recurso, token, **opciones):
    try:
        respuesta = requests.request(metodo, f'{API}/{recurso}', headers=encabezados(token), timeout=15, **opciones)
    except requests.RequestException as error:
        sys.exit(f'No hay conexión con {API}: {error}')
    return respuesta


def imprimir(respuesta):
    """Muestra el código HTTP y el JSON con sangría (como pide el manual). Devuelve el JSON si fue exitoso."""
    print(f'{respuesta.request.method} {respuesta.url}')
    print('Código de estado:', respuesta.status_code)
    try:
        cuerpo = respuesta.json()
    except ValueError:
        cuerpo = None
    if cuerpo is not None:
        print(json.dumps(cuerpo, indent=4, ensure_ascii=False))
    if respuesta.status_code == 401:
        print('\n401: el token es inválido o venció (dura 12 horas). Copie uno nuevo en https://developer.webex.com')
    elif respuesta.status_code == 409 and 'memberships' in respuesta.url:
        print('\n409: esa persona ya es miembro de la sala.')
    elif not respuesta.ok and cuerpo:
        print('\nError de la API:', cuerpo.get('message', 'sin detalle'))
    return cuerpo if respuesta.ok else None
