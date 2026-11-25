# Reparto de tareas — TI.2.3 APIs Cisco DevNet (GR08)

Integrantes: **Stiven Molina (S)** y **Daniela Tituaña (D)**.
Stiven se encarga de todo lo de **Packet Tracer y Postman** y del repositorio; Daniela de todo lo de
**Python** (Webex y los scripts del controlador). Cada uno revisa el informe del otro antes de entregar.

## Resumen

| # | Tarea | Responsable | Depende de |
|---|-------|-------------|------------|
| 0 | Crear el repositorio en GitHub, invitar a Daniela y subir esta estructura | S | — |
| 1 | Descargar de NetAcad los manuales PDF de 8.6.7, 8.8.2 y 8.8.3 y las actividades `.pka` de 8.8.2 y 8.8.3 | S | — |
| 2 | **Lab 8.8.2 SDN CLI** completo: actividad Packet Tracer, capturas, `software-versions.txt`, informe | S | 1 |
| 3 | **Lab 8.8.3 Partes 1–4**: acceso externo en Packet Tracer, API del controlador, Postman (ticket, network-device, host) y capturas | S | 1 |
| 4 | Pasar a Daniela su correo de Webex (en el 8.6.7 ella lo agrega a la sala) | S | — |
| 5 | **Lab 8.6.7 Webex** completo: ejecutar scripts, capturas, informe | D | 4 |
| 6 | **Lab 8.8.3 Partes 5–6**: scripts de Python en el PC y dentro de Packet Tracer, capturas | D | 3 (misma `.pka`) |
| 7 | Informe 8.8.3: S escribe Introducción, Marco teórico y Partes 1–4; D escribe Partes 5–6, Resultados y Conclusiones | S + D | 3, 6 |
| 8 | Revisión cruzada: S revisa el informe 8.6.7 y D revisa el 8.8.2 | S + D | 2, 5 |
| 9 | Correo de entrega con el enlace de Drive (plantilla `TI.2.3 PAO202651_APIS_CISCO_DEVNET_NRC36883.txt`) | S | 7, 8 |

## Detalle por integrante

### Stiven Molina — Packet Tracer, Postman y repositorio
- [ ] Repositorio en GitHub, invitar a Daniela como colaboradora y subir la estructura (tarea 0).
- [ ] Descargar manuales y `.pka` de NetAcad y compartirlos con Daniela (los PDF del curso no se suben al repo).
- [ ] Pasar a Daniela su correo de Webex (crear cuenta si no la tiene).
- [ ] Lab 8.8.2 completo (ver `02. LAB_8.8.2_SDN_CLI/README.md`):
  - [ ] Partes 1–6 en Packet Tracer con capturas.
  - [ ] `software-versions.txt` con `show version | include RELEASE` de cada equipo.
  - [ ] Guardar la `.pka` terminada como `LAB_8.8.2_SDN_CLI_GR08.pka`.
  - [ ] Informe `INFORME_LAB_8.8.2_SDN_CLI_GR08.docx`.
- [ ] Lab 8.8.3 Partes 1–4 con Postman (importar `04. POSTMAN/LAB_8.8.3_PT_Controller_GR08.postman_collection.json`).
  - [ ] Guardar la `.pka` como `LAB_8.8.3_SDN_REST_GR08.pka` y subirla para que Daniela haga las Partes 5–6.
- [ ] Revisar el informe 8.6.7 de Daniela.
- [ ] Enviar el correo de entrega.

### Daniela Tituaña — Python
- [ ] Lab 8.6.7 (ver `01. LAB_8.6.7_WEBEX/README.md`):
  - [ ] Obtener su token en developer.webex.com y crear `config.json` con el correo de Stiven.
  - [ ] Ejecutar los 7 scripts en orden y tomar las capturas de la lista.
  - [ ] Agregar a Stiven a la sala (Parte 6) y enviar el mensaje Markdown (Parte 7).
  - [ ] Informe `INFORME_LAB_8.6.7_WEBEX_PYTHON_GR08.docx`.
- [ ] Lab 8.8.3 Partes 5 y 6 (ver `03. LAB_8.8.3_SDN_REST/README.md`): ejecutar los scripts sobre la `.pka` de Stiven y tomar capturas.
- [ ] Revisar el informe 8.8.2 de Stiven.

## Formato común de los informes
Las mismas secciones en los tres: Portada (tema, autores, tutor, fecha) · Índice · 1 Introducción ·
2 Objetivos (general y específicos) · 3 Marco teórico · 4 Desarrollo del laboratorio (una sección por
Parte y un subtítulo por Paso, cada uno con su captura y pie de figura) · 5 Resultados ·
6 Conclusiones · 7 Recomendaciones · 8 Referencias (APA 7).

## Flujo de git
1. Cada uno trabaja en su rama: `stiven/lab-8.8.2`, `stiven/lab-8.8.3-postman`, `daniela/lab-8.6.7`, `daniela/lab-8.8.3-python`.
2. Commits pequeños por Parte (`Lab 8.8.2: Parte 3 controlador SDN`).
3. Pull request a `main`; el otro integrante lo revisa y lo aprueba.
4. **Nunca** subir `config.json` ni capturas que muestren el token completo de Webex (recórtelo o tápelo).
5. Los `.docx` y `.pka` son binarios: avisar antes de editar uno que tiene el otro para no pisarse cambios.
