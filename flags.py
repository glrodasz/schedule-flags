# -*- coding: UTF-8 -*-
# 👆 Sin lo de arriba no se puede poner emojis
import pytz
import datetime
import sys

# Esta es la hora local que asume:
local_tz = pytz.timezone('Europe/Stockholm')

# YYYY-MM-DD
# Pon la fecha real o no entenderá cambios de horario (Como cuando Mexico y Colombia cambian 1h)
date_to_convert = sys.argv[1]
# Recuerda: Es la hora de tu PC

date_to_convert = datetime.datetime.strptime(
    date_to_convert, "%Y-%m-%d %H:%M:%S")

print(date_to_convert)
print("Generando bloque de banderas:")
print("")

# En orden de tamaño de mercado/prioridad
zones = [
    ["🇨🇴", "America/Bogota"],
    ["🇦🇷", "America/Buenos_Aires"],
    ["🇲🇽", "America/Mexico_City"],
    ["🇵🇪", "America/Lima"],
    ["🇨🇱", "America/Santiago"],
    ["🇻🇪", "America/Caracas"],
    ["🇧🇴", "America/La_Paz"],
    ["🇪🇨", "America/Guayaquil"],
    ["🇪🇸", "Europe/Madrid"],
    ["🇺🇾", "America/Montevideo"],
]

# Inicializamos el diccionario
times = {"00pm": "X"}

# If you need Brazil:
# ["🇧🇷","America/Sao_Paulo"]

# Los timezones no están derivados de países, sino de ciudades.
# Aunque la prioridad es por país

date_to_convert = local_tz.localize(date_to_convert)

for country in zones:

    dtc = date_to_convert.astimezone(pytz.timezone(country[1]))
    if country[1] == "Europe/Madrid":
        # Imprime la hora en formato de 24 horas y una "H" al final
        dtc = dtc.strftime("%-HH")
    else:
        # Imprime la hora en formato de 12 horas PM/AM
        dtc = dtc.strftime("%-I%p")
    try:
        times[dtc] = times[dtc] + country[0]
    except KeyError:
        times[dtc] = country[0]

    # Si el país es USA en Pacific, agregar el "PT" frente a bandera de US
    if country[1] == "US/Pacific":
        times[dtc] = times[dtc] + " PT"

    times[dtc] = times[dtc] + " "

for time, flag in times.items():
    if flag != "X":
        print(time.lower(), flag.strip())