import socket
import time
SOCK_BUFFER = 128
if __name__ == '__main__':
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    informacion = ('localhost',5000)
    servidor.bind(informacion)
    servidor.listen(1)
    print('Esperando conexión del switch transaccional...')
    cliente, direccion = servidor.accept()
    print('Conexión establecida con el switch en el puerto',f'{informacion[1]}.')
    #(1) LECTURA 
    #Se definirá el tiempo de lecura con time.perfcounter
    lectura_inicio = time.perf_counter()
    #Se define una lista donde se irán guardando los valores con respecto al SOCK_BUFFER
    lista_lectura = []
    with open('./transacciones-2023.txt','r') as archivo_lectura:
        while True:
            lectura = archivo_lectura.read(SOCK_BUFFER)
            if lectura:
                lista_lectura.append(lectura)
            else:
                break
        archivo_lectura.close()
    lectura_fin = time.perf_counter()
    
    #(2) Envio
    #Se definirá el tiempo de envio con time.perfcounter
    envio_inicio = time.perf_counter()
    for cadena in lista_lectura:
        cliente.sendall(cadena.encode('utf-8'))
        while True:
            recibido = cliente.recv(SOCK_BUFFER)
            if recibido:
                break
    cliente.sendall('Terminado'.encode('utf-8'))
        
    envio_fin = time.perf_counter()
    print('El tiempo de lectura fue',f'{lectura_fin - lectura_inicio} segundos.')
    print('El tiempo de envio fue',f'{envio_fin- envio_inicio} segundos.')
    print('Cerrando conexión con el switch transaccional...')
    servidor.close()    
    print('Conexión cerrada.')