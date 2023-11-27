import socket
import time 
SOCK_BUFFER = 128
if __name__ == '__main__':
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    informacion = ('localhost',5002)
    servidor.bind(informacion)
    servidor.listen(1)
    print('Esperando conexión del cliente...')
    cliente, direccion = servidor.accept()
    print('Conexión establecida con el cliente en el puerto',f'{informacion[1]}.')
    
    lista_recepcion = []
    while True:
        recibido = cliente.recv(SOCK_BUFFER).decode('utf-8')
        if recibido == 'Terminado':
            break
        else:
            lista_recepcion.append(recibido)
            cliente.sendall('Proceder'.encode('utf-8'))
    servidor.close()
    
    with open('./transacciones-2023_autB.txt','w') as archivo_escritura:
        for termino in lista_recepcion:
            archivo_escritura.write(termino)
        archivo_escritura.close()