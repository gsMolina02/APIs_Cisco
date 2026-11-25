"""Parte 5, paso 4 - Crear una sala: POST /v1/rooms con {"title": ...}.

El manual pide copiar el ID de la sala nueva para las Partes 6 y 7: el script lo guarda en config.json (room_id).
"""
import webex

cfg = webex.config('room_title')
sala = webex.imprimir(webex.post('rooms', cfg['access_token'], {'title': cfg['room_title']}))
if sala:
    webex.guardar('room_id', sala['id'])
    print(f"\nSala creada: {sala['title']}")
    print('Su ID quedó guardado en config.json como room_id.')
