import socket
import time
import matplotlib.pyplot as plt
SIZE_BUFFER = [64, 128, 256, 512, 1024]

def RetornaGruposSock(Ubicaciontxt, SizeSockBuffer):
    global SOCK_BUFFER
    with open(Ubicaciontxt,'r') as archivo_leido:
        lineas = archivo_leido.readlines()
        archivo_leido.close()
    lineas_separadas = []
    for linea in lineas:
        linea_arreglada = (linea.replace('[',' ').replace(']',' ')).split(' ')
        if linea == '*****\n':
            lineas_separadas.append(linea)
        else:
            if (linea_arreglada[6] == 'B040') or  (linea_arreglada[6] == 'B020') or  (linea_arreglada[6] == 'B013') or  (linea_arreglada[6] == 'B012') or  (linea_arreglada[6] == 'B010'):
                lineas_separadas.append(linea)

    grupos_sock_buffer = []
    grupo_individual = ''
    for linea in lineas_separadas:
        if len(linea) + len(grupo_individual) < SizeSockBuffer:
            grupo_individual = grupo_individual + linea
        else:
            bits_necesarios = SOCK_BUFFER - (len(grupo_individual) - 1)
            grupo_individual = grupo_individual + linea[0:bits_necesarios-1]
            grupos_sock_buffer.append(grupo_individual)
            grupo_individual = linea[bits_necesarios-1: len(linea)]
    if grupo_individual:
        grupos_sock_buffer.append(grupo_individual)
    return grupos_sock_buffer


if __name__ == '__main__':
    #En este caso, vamos enviar las cadenas de texto de tamaño SOCK_BUFFER a cada servidor
    #Usaremos la función definida al inicio para obtener los paquetes de tamaño SOCK_BUFFER
    ClienteA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClienteA.connect(('localhost',5001))
    print('Conexión establecida con la autorización A.')
    tiempos_totales = []
    for SOCK_BUFFER in SIZE_BUFFER:
        Lista_arregloA = RetornaGruposSock('./transacciones-2023_autA.txt', SOCK_BUFFER)
        inicio = time.perf_counter()
        for cadena in Lista_arregloA:
            ClienteA.sendall(cadena.encode('utf-8'))
            while True:
                recibido = ClienteA.recv(SOCK_BUFFER)
                if recibido:
                    break
        ClienteA.sendall('Terminado'.encode('utf-8'))
        fin = time.perf_counter()
        tiempos_totales.append(fin-inicio)
    print('Cerrando conexión desde servidor...')
    ClienteA.close()
    print('Conexión cerrada con la autorización A.')
    plt.plot(SIZE_BUFFER, tiempos_totales)
    plt.xlabel('Tamaño de buffer')
    plt.ylabel('Tiempo (s)')
    plt.title('Relación de tamaño de buffer vs tiempo de envío A')
    plt.savefig('Relación_envíoA')
    plt.close()

    ClienteB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClienteB.connect(('localhost',5002))
    print('Conexión establecida con la autorización B.')
    tiempos_totales = []
    for SOCK_BUFFER in SIZE_BUFFER:
        Lista_arregloA = RetornaGruposSock('./transacciones-2023_autB.txt', SOCK_BUFFER)
        inicio = time.perf_counter()
        for cadena in Lista_arregloA:
            ClienteB.sendall(cadena.encode('utf-8'))
            while True:
                recibido = ClienteB.recv(SOCK_BUFFER)
                if recibido:
                    break
        ClienteB.sendall('Terminado'.encode('utf-8'))
        fin = time.perf_counter()
        tiempos_totales.append(fin-inicio)
    print('Cerrando conexión desde servidor...')
    ClienteB.close()
    print('Conexión cerrada con la autorización B.')
plt.plot(SIZE_BUFFER, tiempos_totales)
plt.xlabel('Tamaño de buffer')
plt.ylabel('Tiempo (s)')
plt.title('Relación de tamaño de buffer vs tiempo de envío B')
plt.savefig('Relación_envíoB')