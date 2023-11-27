import socket
import time
SOCK_BUFFER = 128
if __name__ == '__main__':
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost',5000))
    print('Conexión establecida con la base de datos.')
    #(1) RECEPCION
    recepcion_inicio = time.perf_counter()
    lista_recepcion = []
    while True:
        recibido = cliente.recv(SOCK_BUFFER).decode('utf-8')
        if recibido == 'Terminado':
            break
        else:
            lista_recepcion.append(recibido)
            cliente.sendall('Proceder'.encode('utf-8'))
    recepcion_fin = time.perf_counter()
    #(2) ESCRITURA
    escritura_inicio = time.perf_counter()
    with open('./transacciones-2023.txt','w') as archivo_escritura:
        for termino in lista_recepcion:
            archivo_escritura.write(termino)
        archivo_escritura.close()
    escritura_fin = time.perf_counter()
    print('El tiempo de recepción fue',f'{recepcion_fin- recepcion_inicio} segundos.')      
    print('El tiempo de escritura fue',f'{escritura_fin-escritura_inicio} segundos.')
    print('Cerrando conexión desde servidor...')
    cliente.close()
    print('Conexión cerrada con la base de datos.')