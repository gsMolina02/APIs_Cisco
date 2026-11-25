"""Parte 4 - Gestionar personas: GET /v1/people?email=<correo> devuelve los detalles de un usuario de Webex."""
import webex

cfg = webex.config('person_email')
datos = webex.imprimir(webex.get('people', cfg['access_token'], email=cfg['person_email']))
if datos is not None:
    if datos['items']:
        persona = datos['items'][0]
        print(f"\nEncontrado: {persona['displayName']} | id: {persona['id']}")
    else:
        print(f"\nNo hay ningún usuario de Webex con el correo {cfg['person_email']}.")
