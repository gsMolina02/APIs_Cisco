"""Parte 3 - Probar el token de acceso: GET /v1/people/me devuelve los datos del dueño del token."""
import webex

cfg = webex.config()
yo = webex.imprimir(webex.get('people/me', cfg['access_token']))
if yo:
    print(f"\nToken válido. Usuario autenticado: {yo['displayName']} ({', '.join(yo['emails'])})")
