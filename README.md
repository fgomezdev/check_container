# check_container
Verifica si un contenedor docker está activo y notifica mediante un webhook a Discord

python check_container.py --name="{nombre_del_contenedor_a_controlar}" --webhook="{discord_webhook}" --alias="{prefijo_para_mensajes}" --period={tiempo_entre_consultas_en_Segundos}


docker run --name check_container --rm -d -v /var/run/docker.sock:/var/run/docker.sock check_container:1.0 --name="{nombre_del_contenedor_a_controlar}" --webhook="{discord_webhook}" --alias="{prefijo_para_mensajes}" --period={tiempo_entre_consultas_en_segundos}