"""Parte 5, paso 2 - Solicitar un ticket de servicio: POST /api/v1/ticket."""
import controlador

ticket = controlador.obtener_ticket()
print('Ticket de servicio:', ticket)
