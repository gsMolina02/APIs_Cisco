# Lab 8.6.7 — Python para administrar equipos de Webex

**Responsable: Daniela** · Necesita: Python 3.10+, cuenta en Webex y el correo Webex de Stiven.

## Preparar (una sola vez)
```powershell
cd "01. LAB_8.6.7_WEBEX\02. SCRIPTS PYTHON"
pip install -r requirements.txt
copy config.example.json config.json
```
1. Inicie sesión en https://developer.webex.com → **Documentation → Getting started** → copie su
   *Personal Access Token* (dura 12 horas).
2. Péguelo en `config.json` (`access_token`) y escriba el correo Webex de Stiven en `person_email`.
   `config.json` no se sube a git.

## Ejecutar (en este orden)
| Parte | Script | API | Qué capturar |
|-------|--------|-----|--------------|
| 3 | `python authentication.py` | GET /people/me | `P3_token_docs.png` (Try it en la documentación) y `P3_authentication.png` |
| 4 | `python list-people.py` | GET /people?email= | `P4_list_people_docs.png` y `P4_list_people.png` |
| 5.2 | `python list-rooms.py` | GET /rooms | `P5_list_rooms.png` |
| 5.4 | `python create-rooms.py` | POST /rooms | `P5_create_room.png` (guarda `room_id` en config.json) |
| 6.2 | `python list-memberships.py` | GET /memberships?roomId= | `P6_list_memberships.png` (solo usted) |
| 6.4 | `python create-membership.py` | POST /memberships | `P6_create_membership.png` y otra vez `list-memberships.py` → `P6_miembros_final.png` |
| 7 | `python create-markdown-message.py` | POST /messages | `P7_mensaje_script.png` y `P7_mensaje_app.png` (mensaje en la app de Webex con negritas) |

Además: `P1_scripts_vscode.png` (carpeta abierta en VS Code) y `P2_developer_webex.png`.

> **Antes de capturar**, tape o recorte el token completo: es una credencial personal.

Guarde las capturas en `01. DOCUMENTACION/capturas/` y el informe como
`01. DOCUMENTACION/INFORME_LAB_8.6.7_WEBEX_PYTHON_GR08.docx`.

## Errores comunes
- **401**: token vencido → copie uno nuevo.
- **409 en create-membership**: Stiven ya es miembro de la sala.
- `list-people.py` sin resultados: el correo no tiene cuenta de Webex todavía.
