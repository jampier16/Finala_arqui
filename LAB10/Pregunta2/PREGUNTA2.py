#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
import threading
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""
def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])

def funcion1():
	variable_i = 0
	Paises = ["UK","España","Estados Unidos","Hong Kong","Japón"]
	pais_menor = 24
	for servidor in servidores_ntp:
		tiempo = get_ntp_time(servidor)
		tiempo_horas = tiempo.hour + tiempo.minute/60 + tiempo. second/3600
		if(tiempo_horas > 8):
			tiempo_faltante = 24 - (tiempo_horas - 8)
		else:
			tiempo_faltante = 8 - tiempo_horas
		if (tiempo_faltante < pais_menor):
			pais_menor = tiempo_faltante
			indice = variable_i
		variable_i += 1
	print("El pais más cercano a a abrir es", Paises[indice],"en",pais_menor,"horas")


	

if __name__ == '__main__':
    #a)
    tem1=[]
    tem1i=time.perf_counter()
    funcion1()
    tem1f=time.perf_counter()
    print("tiempor de ejecucion: ", tem1f-tem1i)