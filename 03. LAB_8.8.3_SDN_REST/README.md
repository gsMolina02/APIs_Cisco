# Lab 8.8.3 — API REST de un controlador SDN con Postman y Python

**Partes 1–4: Stiven (Packet Tracer + Postman) · Partes 5–6: Daniela (Python)**
Necesita: Packet Tracer 8.2+, Postman, Python 3.10+ y la actividad `.pka` de NetAcad.

Stiven guarda la actividad como `02. PACKET TRACER/LAB_8.8.3_SDN_REST_GR08.pka` y la sube a git;
Daniela trabaja las Partes 5–6 sobre esa misma copia.

## Partes 1–2 — Preparar y verificar el acceso externo (Stiven)
- [ ] Carpeta del laboratorio abierta en VS Code (`P1_scripts_vscode.png`).
- [ ] Options → Preferences → Miscellaneous → **External Network Access** (`P2_preferences.png`).
- [ ] PT-Controller0 → Config → Controller → **Access Enabled**, puerto 58000 (`P2_controller_listening.png`).
- [ ] En el navegador `http://localhost:58000/api/v1/host` responde *empty ticket* (`P2_navegador_sin_ticket.png`).

## Partes 3–4 — Postman (Stiven)
Importe `04. POSTMAN/LAB_8.8.3_PT_Controller_GR08.postman_collection.json` y ejecute en orden:
- [ ] Documentación `addTicket` en la página del controlador (`P3_api_docs.png`).
- [ ] `1. POST ticket` → 201 y el ticket queda guardado solo (`P3_postman_ticket.png`).
- [ ] `2. GET network-device` (`P4_postman_network_device.png`).
- [ ] `3. GET host` (`P4_postman_host.png`).

## Parte 5 — Python en el PC (Daniela)
```powershell
cd "03. LAB_8.8.3_SDN_REST\03. SCRIPTS PYTHON"
pip install -r requirements.txt
python 01_get-ticket.py           # P5_get_ticket.png
python 02_get-network-device.py   # P5_network_device.png
python 03_get-host.py             # P5_host.png
```
Si registraron otro usuario en el controlador: `$env:PT_USUARIO="..."; $env:PT_CLAVE="..."`.

## Parte 6 — Python dentro de Packet Tracer (Daniela)
- [ ] En el PC de administración → **Programming** → nuevo proyecto *REST API* (Python).
- [ ] Pegar `packet_tracer/main_network_device.py` en `main.py` y Run (`P6_programming_network_device.png`).
- [ ] Pegar `packet_tracer/main_host.py` y Run (`P6_programming_host.png`).
- [ ] **Check Results** al 100 % (`Fin_check_results.png`).

## Entregables
- `02. PACKET TRACER/LAB_8.8.3_SDN_REST_GR08.pka`
- `01. DOCUMENTACION/capturas/*.png`
- `01. DOCUMENTACION/INFORME_LAB_8.8.3_SDN_REST_GR08.docx` (reparto de secciones en `TAREAS.md`)
