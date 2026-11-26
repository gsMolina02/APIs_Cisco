# Lab 8.8.2 — Administración de la red por CLI y con un controlador SDN

**Responsable: Stiven** · Necesita: Cisco Packet Tracer 8.2 o superior.

Trabaje sobre `02. PACKET TRACER/LAB_8.8.2_SDN_CLI_GR08.pka` (copia de la actividad original de NetAcad).
Siga el manual; esta es la lista de lo que debe quedar documentado en el informe, un subtítulo por
paso (nombre de cada captura entre paréntesis). Credenciales de toda la actividad: `cisco` / `cisco123!`.

## Parte 1 — Explorar la topología
- [ ] Paso 1: topología completa y documentación de la red (`P1_topologia.png`).
- [ ] Paso 2: pings entre dispositivos con PDU simple o CLI (`P1_pdu_simple.png`, `P1_pings.png`).

## Parte 2 — Recopilar información por CLI (método tradicional)
- [ ] Paso 1: Admin > Command Prompt > `ssh -l cisco 10.0.1.4` (SWR3) (`P2_ssh_swr3.png`).
- [ ] Paso 2: `show version | include RELEASE` en SWR3 y pegarlo en el bloc de notas (`P2_version_swr3.png`).
- [ ] Paso 3: desde SWR3, SSH a los otros 8 equipos y repetir (`P2_ssh_otro.png`);
      `01. DOCUMENTACION/software-versions.txt` completo (`P2_software_versions.png`).

## Parte 3 — Configurar el controlador SDN (PT-Controller0)
- [ ] Paso 1: agregar el Network Controller a la izquierda de SWL1 y cablearlo (`P3_controlador_agregado.png`).
- [ ] Paso 2: gateway 192.168.101.1, IP 192.168.101.254/24 (`P3_gateway.png`, `P3_config_ip.png`);
      Preferences > Miscellaneous > acceso externo (`P3_preferences.png`); Access Enabled, puerto 58000 (`P3_api_listening.png`).
- [ ] Paso 3: ping de Admin a 192.168.101.254 (`P3_ping.png`).
- [ ] Paso 4: navegador de Admin > 192.168.101.254, registrar usuario, login y dashboard
      (`P3_registro_usuario.png`, `P3_dashboard.png`).

## Parte 4 — Descubrir la red
- [ ] Paso 1: Provisioning > CREDENTIAL > +CREDENTIAL (`P4_credencial.png`).
- [ ] Paso 2: DISCOVERY "SWL1", IP 192.168.101.2, en curso y terminado (`P4_discovery_en_curso.png`, `P4_discovery.png`).

## Parte 5 — Recopilar información con el controlador
- [ ] Paso 1: Network Device con los 9 equipos y detalle de uno (`P5_network_devices.png`, `P5_detalle_dispositivo.png`).
- [ ] Paso 2: dashboard al 100 % y HOSTS (`P5_dashboard_100.png`, `P5_hosts.png`).
- [ ] Paso 3: Topology (`P5_topologia.png`).
- [ ] Paso 4: TRACE PATH de PC1 a PC4 (`P5_trace_path.png`).

## Parte 6 — Configurar la red desde el controlador
- [ ] Paso 1: Servidor de ejemplo > Services: DNS, Syslog, NTP (`P6_srv_dns.png`, `P6_srv_syslog.png`, `P6_srv_ntp.png`).
- [ ] Paso 2: Policy > Network Settings: DNS, NTP, Syslog y PUSH CONFIG
      (`P6_dns.png`, `P6_ntp.png`, `P6_syslog.png`, `P6_push.png`).
- [ ] Paso 3: en R1 por CLI `show run | begin ip domain`, `show ntp associations`, `show clock`,
      `show run | include logging` (`P6_cli_dns.png`, `P6_cli_ntp.png`, `P6_cli_logging.png`);
      shutdown / no shutdown de S0/1/0 (`P6_shutdown.png`) y mensajes en el servidor Syslog (`P6_syslog_servidor.png`).
- [ ] **Check Results** de la actividad (`Fin_check_results.png`).

## Entregables
- `02. PACKET TRACER/LAB_8.8.2_SDN_CLI_GR08.pka`
- `01. DOCUMENTACION/software-versions.txt`
- `01. DOCUMENTACION/capturas/*.png`
- `01. DOCUMENTACION/INFORME_LAB_8.8.2_SDN_CLI_GR08.docx`

En las **Conclusiones** compare ambos métodos: por CLI hubo que entrar a cada equipo por SSH; con el
controlador se descubrió la red y se aplicó una política a todos los equipos de una sola vez.
