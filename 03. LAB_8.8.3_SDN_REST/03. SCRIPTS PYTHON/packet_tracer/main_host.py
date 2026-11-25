# Parte 6 - Pegar en Packet Tracer: PC de administración > Programming > proyecto "REST API" (Python) > main.py > Run.
# Dentro de Packet Tracer se usa la IP del controlador en la topología (sin el puerto 58000 del PC).
import json
import requests

API = "http://192.168.101.254/api/v1"

r = requests.post(API + "/ticket",
                  json.dumps({"username": "cisco", "password": "cisco123!"}),
                  headers={"content-type": "application/json"})
print("POST /ticket -> " + str(r.status_code))
ticket = r.json()["response"]["serviceTicket"]

r = requests.get(API + "/host", headers={"X-Auth-Token": ticket})
print("GET /host -> " + str(r.status_code))
for h in r.json()["response"]:
    print(h["hostName"] + "\t" + h["hostIp"] + "\t" + h["hostMac"] + "\t" + h["connectedInterfaceName"])
