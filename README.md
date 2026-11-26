# TI.2.3 — APIs Cisco DevNet (GR08)

**Arquitectura de Software · NRC 36883 · PAO 202651**
Integrantes: **Stiven Molina** y **Daniela Tituaña** · Tutor: Ing. Mauricio Campaña

Tres laboratorios del curso Cisco DevNet Associate. En cada uno se ejecuta el manual de NetAcad,
se guardan las capturas y se entrega un informe.

| Carpeta | Laboratorio | Herramientas | Responsable | Estado |
|---------|-------------|--------------|-------------|--------|
| `01. LAB_8.6.7_WEBEX/` | 8.6.7: Python para administrar equipos de Webex | Python 3 + `requests` + cuenta Webex | Daniela | Scripts listos; falta ejecutar, capturas e informe |
| `02. LAB_8.8.2_SDN_CLI/` | 8.8.2: administración de red por CLI vs. controlador SDN | Cisco Packet Tracer 8.2+ | Stiven | Por hacer |
| `03. LAB_8.8.3_SDN_REST/` | 8.8.3: API REST del controlador SDN | Packet Tracer + Postman + Python | Stiven | Scripts y colección listos; falta ejecutar, capturas e informe |

Cada laboratorio tiene su propio `README.md` con los pasos y la lista de capturas del informe.

## Estructura

```
TI.2.3. APIs_CISCO_DEVNET_NRC36883_GR08/
├── 01. LAB_8.6.7_WEBEX/
│   ├── 01. DOCUMENTACION/        informe .docx + capturas/
│   └── 02. SCRIPTS PYTHON/       scripts del manual + webex.py (módulo común)
├── 02. LAB_8.8.2_SDN_CLI/
│   ├── 01. DOCUMENTACION/        informe .docx + capturas/ + software-versions.txt
│   └── 02. PACKET TRACER/        actividad .pka terminada
├── 03. LAB_8.8.3_SDN_REST/
│   ├── 01. DOCUMENTACION/        informe .docx + capturas/
│   ├── 02. PACKET TRACER/        actividad .pka terminada
│   ├── 03. SCRIPTS PYTHON/       scripts para el PC y para Packet Tracer
│   └── 04. POSTMAN/              colección de Postman
├── README.md
└── .gitignore
```

## Datos privados

`config.json` (token de Webex, correos, IDs de sala) **no se sube a git** (`.gitignore`).
Cada integrante copia `config.example.json` como `config.json` y pone sus propios datos.
El token de Webex vence a las 12 horas: si un script responde 401, copie uno nuevo de
https://developer.webex.com.
