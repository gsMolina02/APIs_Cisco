"""Parte 7 - Enviar un mensaje con formato Markdown a la sala: POST /v1/messages con roomId y markdown."""
import webex

cfg = webex.config('room_id', 'message')
mensaje = webex.imprimir(webex.post('messages', cfg['access_token'],
                                    {'roomId': cfg['room_id'], 'markdown': cfg['message']}))
if mensaje:
    print('\nMensaje enviado. Ábralo en la app de Webex para ver el formato Markdown (negritas).')
