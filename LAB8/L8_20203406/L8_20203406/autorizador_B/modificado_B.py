import socket
import time 
import matplotlib.pyplot as plt
SIZE_BUFFER = [64, 128, 256, 512, 1024]
if __name__ == '__main__':
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    informacion = ('localhost',5002)
    servidor.bind(informacion)
    servidor.listen(1)
    print('Esperando conexión del cliente...')
    cliente, direccion = servidor.accept()
    print('Conexión establecida con el cliente en el puerto',f'{informacion[1]}.')
    tiempos_recepcion = []
    for SOCK_BUFFER in SIZE_BUFFER:
        lista_recepcion = []
        inicio = time.perf_counter()
        while True:
            recibido = cliente.recv(SOCK_BUFFER).decode('utf-8')
            if recibido == 'Terminado':
                break
            else:
                lista_recepcion.append(recibido)
                cliente.sendall('Proceder'.encode('utf-8'))
        fin = time.perf_counter()
        tiempos_recepcion.append(fin-inicio)
    servidor.close()
    
    plt.plot(SIZE_BUFFER, tiempos_recepcion)
    plt.xlabel('Tamaño de buffer')
    plt.ylabel('Tiempo (s)')
    plt.title('Relación de tamaño de buffer vs tiempo de recepción B')
    plt.savefig('Relación_recepción')
        
