# Lab 8.8.3 — API REST de un controlador SDN con Postman y Python

**Responsable: Stiven** (todas las partes)
Necesita: Packet Tracer 8.2+, Postman, Python 3.10+ y la actividad `.pka` de NetAcad.

Trabaje sobre `02. PACKET TRACER/LAB_8.8.3_SDN_REST_GR08.pka` (copia de la actividad original de NetAcad).

**Adaptación:** el manual usa la VM DEVASC (Parte 1). Aquí todo se hace directo en Windows (Packet Tracer,
Postman, VS Code y Python 3 en el mismo PC), así que la Parte 1 se documenta como preparación del entorno.

## Partes 1–2 — Preparar y verificar el acceso externo
- [ ] Parte 1: carpeta de scripts abierta en VS Code y `python --version` (`P1_scripts_vscode.png`).
- [ ] Options → Preferences → Miscellaneous → **External Network Access** (`P2_preferences.png`).
- [ ] PT-Controller0 → Config → Controller → **Access Enabled**, puerto 58000 (`P2_controller_listening.png`).
- [ ] En el navegador `http://localhost:58000/api/v1/host` responde *empty ticket* (`P2_navegador_sin_ticket.png`).

## Partes 3–4 — Postman
Importe `04. POSTMAN/LAB_8.8.3_PT_Controller_GR08.postman_collection.json` y ejecute en orden:
- [ ] Documentación `addTicket` en la página del controlador (`P3_api_docs.png`).
- [ ] `1. POST ticket` → 201 y el ticket queda guardado solo (`P3_postman_ticket.png`).
- [ ] `2. GET network-device` (`P4_postman_network_device.png`).
- [ ] `3. GET host` (`P4_postman_host.png`).

## Parte 5 — Python en el PC
```powershell
cd "03. LAB_8.8.3_SDN_REST\03. SCRIPTS PYTHON"
pip install -r requirements.txt
python 01_get-ticket.py           # P5_get_ticket.png
python 02_get-network-device.py   # P5_network_device.png
python 03_get-host.py             # P5_host.png
```
Si registraron otro usuario en el controlador: `$env:PT_USUARIO="..."; $env:PT_CLAVE="..."`.

## Parte 6 — Python dentro de Packet Tracer
- [ ] En el PC de administración → **Programming** → New → nombre *API REST*, plantilla *Empty - Python* → Create.
- [ ] Pegar `packet_tracer/main_network_device.py` en `main.py` y Run (`P6_programming_network_device.png`).
- [ ] Pegar `packet_tracer/main_host.py` y Run (`P6_programming_host.png`).
- [ ] **Check Results** al 100 % (`Fin_check_results.png`).

## Entregables
- `02. PACKET TRACER/LAB_8.8.3_SDN_REST_GR08.pka`
- `01. DOCUMENTACION/capturas/*.png`
- `01. DOCUMENTACION/INFORME_LAB_8.8.3_SDN_REST_GR08.docx`
