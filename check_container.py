from datetime import datetime
import time

import argparse
from discord import Webhook, RequestsWebhookAdapter
import docker

def docker_verificar_estado(nombre_contenedor):
    ESTADO_ESPERADO = "running"
    cliente = docker.from_env()

    try:
        contenedor = cliente.containers.get(nombre_contenedor)
    except docker.errors.NotFound as exc:
        print(f"Contenedor no encontrado: {exc.explanation}")
    except Exception as ex:
        print(f"Error desconocido: {ex}")
    else:
        return contenedor.attrs["State"]["Status"] == ESTADO_ESPERADO

    return False


def enviar_notificacion(mensaje, webhook):
    webhook = Webhook.from_url(webhook, adapter=RequestsWebhookAdapter())
    webhook.send(mensaje)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Controla si el contenedor está activo e informa cuando éste se detiene mediante mensaje a webhook de discord.')
    parser.add_argument('--name', help='Nombre del contenedor')
    parser.add_argument('--alias', help='Prefijo para los mensajes', default="")
    parser.add_argument('--webhook', help='Url del webhook de discord')
    parser.add_argument('--period', help='Tiempo entre consultas (en segundos)', type=int, default=60*5)
    args = parser.parse_args()

    nombre_contenedor = args.name
    alias = args.alias
    webhook = args.webhook
    period = args.period

    contenedor_activo = True
    running = False
    
    while True:        
        hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        alias_name = "" if alias == "" else f"**{alias.upper()}** "
        if not running:
            running = True
            mensaje = f"{alias_name}{hora}: Iniciando CheckContainer para el contenedor **{nombre_contenedor}**"
            enviar_notificacion(mensaje, webhook)
            time.sleep(10)

        contenedor_activo = docker_verificar_estado(nombre_contenedor)
        mensaje = f"{alias_name}{hora}: **{nombre_contenedor}** Activo: {contenedor_activo}"
        print(mensaje)

        if not contenedor_activo:
            break
        time.sleep(period)

    enviar_notificacion(mensaje, webhook)
