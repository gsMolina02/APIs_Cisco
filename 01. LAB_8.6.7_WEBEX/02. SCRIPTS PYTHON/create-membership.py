"""Parte 6, paso 4 - Agregar a un compañero a la sala: POST /v1/memberships con roomId y personEmail."""
import webex

cfg = webex.config('room_id', 'person_email')
miembro = webex.imprimir(webex.post('memberships', cfg['access_token'],
                                    {'roomId': cfg['room_id'], 'personEmail': cfg['person_email']}))
if miembro:
    print(f"\n{miembro['personDisplayName']} fue agregado a la sala.")
