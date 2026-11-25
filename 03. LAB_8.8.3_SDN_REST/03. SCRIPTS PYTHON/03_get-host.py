"""Parte 5, paso 4 - Listar los hosts: GET /api/v1/host."""
import controlador

ticket = controlador.obtener_ticket()
hosts = controlador.consultar('host', ticket)
controlador.tabla(hosts, [('Host', 'hostName'), ('IP', 'hostIp'), ('MAC', 'hostMac'),
                          ('Conectado a', 'connectedNetworkDeviceIpAddress'), ('Interfaz', 'connectedInterfaceName')])
