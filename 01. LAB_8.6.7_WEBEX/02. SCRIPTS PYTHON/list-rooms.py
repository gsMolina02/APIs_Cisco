"""Parte 5, paso 2 - Listar las salas del usuario: GET /v1/rooms?max=100."""
import webex

cfg = webex.config()
datos = webex.imprimir(webex.get('rooms', cfg['access_token'], max=100))
if datos is not None:
    print(f"\n{len(datos['items'])} sala(s):")
    for sala in datos['items']:
        print(f"  - {sala['title']:<40} {sala['type']:<7} {sala['id']}")
