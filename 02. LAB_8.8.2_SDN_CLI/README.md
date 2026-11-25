# Lab 8.8.2 — Administración de la red por CLI y con un controlador SDN

**Responsable: Stiven** · Necesita: Cisco Packet Tracer 8.2 o superior y la actividad `.pka` de NetAcad.

Abra la actividad original, guárdela de inmediato como `02. PACKET TRACER/LAB_8.8.2_SDN_CLI_GR08.pka`
y trabaje sobre esa copia. Siga el manual de NetAcad; esta es la lista de lo que debe quedar
documentado en el informe (nombre sugerido de cada captura entre paréntesis).

## Parte 1 — Explorar la topología
- [ ] Topología completa (`topologia.png`).
- [ ] Hosts sin dirección correcta y su corrección a DHCP (`P1_dhcp_antes.png`, `P1_dhcp_despues.png`).
- [ ] Pings entre hosts de distintas LAN (`P1_pings.png`).

## Parte 2 — Recopilar información por CLI (método tradicional)
- [ ] SSH desde el PC de administración a SWR3 y `show version | include RELEASE` (`P2_ssh_swr3.png`).
- [ ] Lo mismo en otro equipo (`P2_ssh_otro.png`).
- [ ] Llenar `01. DOCUMENTACION/software-versions.txt` con la versión de **cada** switch y router.
  (Muestra lo lento que es el método manual: es el punto que compara el laboratorio.)

## Parte 3 — Configurar el controlador SDN (PT-Controller0)
- [ ] Agregar el controlador y configurar su IP según el manual (`P3_config_ip.png`).
- [ ] Config → Controller → **Access Enabled** (`P3_api_listening.png`).
- [ ] Ping desde el PC al controlador (`P3_ping.png`) y conexión al panel web (`P3_controlador_conectado.png`).
- [ ] Registrar el usuario del controlador e iniciar sesión (`P3_panel.png`).

## Parte 4 — Descubrir la red
- [ ] Registrar las credenciales CLI de los equipos (`P4_credencial.png`).
- [ ] Discovery por CDP y equipos descubiertos (`P4_discovery.png`).

## Parte 5 — Recopilar información con el controlador
- [ ] Network Devices (`P5_network_devices.png`) y detalle de un equipo (`P5_detalle_dispositivo.png`).
- [ ] Hosts (`P5_hosts.png`), Topology (`P5_topologia.png`) y Path Trace entre dos hosts (`P5_trace_path.png`).

## Parte 6 — Configurar la red desde el controlador
- [ ] Servicios del servidor de ejemplo (`P6_servicios_servidor.png`).
- [ ] Política global: DNS, NTP y Syslog (`P6_dns.png`, `P6_ntp.png`, `P6_syslog.png`).
- [ ] Enviar la configuración (push) (`P6_push.png`) y verificar en R1 por CLI (`P6_cli_r1.png`).
- [ ] Generar un evento y verlo en el servidor Syslog (`P6_syslog_servidor.png`).
- [ ] **Check Results** de la actividad al 100 % (`Fin_check_results.png`).

## Entregables
- `02. PACKET TRACER/LAB_8.8.2_SDN_CLI_GR08.pka`
- `01. DOCUMENTACION/software-versions.txt`
- `01. DOCUMENTACION/capturas/*.png`
- `01. DOCUMENTACION/INFORME_LAB_8.8.2_SDN_CLI_GR08.docx` (secciones en `TAREAS.md`)

En las **Conclusiones** compare ambos métodos: por CLI hubo que entrar a cada equipo por SSH; con el
controlador se descubrió la red y se aplicó una política a todos los equipos de una sola vez.
