"""Parte 6, paso 2 - Listar los miembros de la sala: GET /v1/memberships?roomId=<id>.

Nota: el parámetro es roomId (con r minúscula); con otra forma la API ignora el filtro.
"""
import webex

cfg = webex.config('room_id')
datos = webex.imprimir(webex.get('memberships', cfg['access_token'], roomId=cfg['room_id']))
if datos is not None:
    print(f"\n{len(datos['items'])} miembro(s):")
    for miembro in datos['items']:
        moderador = ' (moderador)' if miembro.get('isModerator') else ''
        print(f"  - {miembro['personDisplayName']} <{miembro['personEmail']}>{moderador}")
