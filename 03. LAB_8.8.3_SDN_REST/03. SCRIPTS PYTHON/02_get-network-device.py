"""Parte 5, paso 3 - Listar los dispositivos de red: GET /api/v1/network-device.

El ticket se pide al iniciar (el manual lo copia a mano en el código; así no vence entre ejecuciones).
"""
import controlador

ticket = controlador.obtener_ticket()
dispositivos = controlador.consultar('network-device', ticket)
controlador.tabla(dispositivos, [('Hostname', 'hostname'), ('Plataforma', 'platformId'),
                                 ('IP de administración', 'managementIpAddress'), ('Estado', 'reachabilityStatus')])
