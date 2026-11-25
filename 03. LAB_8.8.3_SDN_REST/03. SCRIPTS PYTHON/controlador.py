"""Cliente de la API REST northbound del controlador SDN PT-Controller0 (laboratorio 8.8.3, GR08).

Packet Tracer publica la API del controlador en el PC en http://localhost:58000/api/v1 cuando:
  1. Options > Preferences > Miscellaneous > External Network Access está habilitado, y
  2. PT-Controller0 > Config > Controller tiene marcado Access Enabled.

Las credenciales por defecto son las del manual (cisco / cisco123!). Si registraron otras, use
las variables de entorno PT_USUARIO y PT_CLAVE; PT_API cambia la dirección base.
"""
import json
import os
import sys

try:
    import requests
except ImportError:
    sys.exit('Falta la librería requests. Instálela con:  pip install -r requirements.txt')

API = os.environ.get('PT_API', 'http://localhost:58000/api/v1')
USUARIO = os.environ.get('PT_USUARIO', 'cisco')
CLAVE = os.environ.get('PT_CLAVE', 'cisco123!')


def obtener_ticket():
    """POST /ticket con usuario y clave. Devuelve el serviceTicket que autoriza las demás consultas."""
    try:
        respuesta = requests.post(f'{API}/ticket', json={'username': USUARIO, 'password': CLAVE}, timeout=10)
    except requests.ConnectionError:
        sys.exit(f'Nadie responde en {API}.\n'
                 'Abra la actividad en Packet Tracer y marque Access Enabled en PT-Controller0 > Config > Controller.')
    print('POST /ticket ->', respuesta.status_code)
    cuerpo = respuesta.json()
    if respuesta.status_code != 201:
        sys.exit('No se obtuvo el ticket: ' + json.dumps(cuerpo.get('response', cuerpo), ensure_ascii=False))
    return cuerpo['response']['serviceTicket']


def consultar(recurso, ticket):
    """GET /<recurso> enviando el ticket en el encabezado X-Auth-Token. Devuelve la lista 'response'."""
    respuesta = requests.get(f'{API}/{recurso}', headers={'X-Auth-Token': ticket}, timeout=10)
    print(f'GET /{recurso} ->', respuesta.status_code)
    cuerpo = respuesta.json()
    if respuesta.status_code != 200:
        sys.exit('Error de la API: ' + json.dumps(cuerpo.get('response', cuerpo), ensure_ascii=False))
    return cuerpo['response']


def tabla(filas, columnas):
    """Imprime una lista de diccionarios como tabla con las columnas (titulo, clave) indicadas."""
    anchos = [max(len(titulo), *(len(str(f.get(clave, ''))) for f in filas)) if filas else len(titulo)
              for titulo, clave in columnas]
    print()
    print('  '.join(titulo.ljust(ancho) for (titulo, _), ancho in zip(columnas, anchos)))
    print('  '.join('-' * ancho for ancho in anchos))
    for fila in filas:
        print('  '.join(str(fila.get(clave, '')).ljust(ancho) for (_, clave), ancho in zip(columnas, anchos)))
    print(f'\nTotal: {len(filas)}')
