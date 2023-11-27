import socket
import time
SOCK_BUFFER = 128

def RetornaGruposSock(Ubicaciontxt):
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
        if len(linea) + len(grupo_individual) < SOCK_BUFFER:
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
    #Creamos los archivos de texto a partir de lo leido
    with open('./transacciones-2023.txt','r') as archivo_lectura:
        lineas_total = archivo_lectura.readlines()
        archivo_lectura.close()    
    grupo_asterisco = []
    total_grupos_A = []
    total_grupos_B = []
    for linea in lineas_total:
        grupo_asterisco.append(linea)
        if (linea == '*****\n') or (linea == lineas_total[len(lineas_total) - 1]):
            if (linea == '*****\n'):
                linea_examinada = grupo_asterisco[len(grupo_asterisco) - 2]
            if (linea == lineas_total[len(lineas_total) - 1]):
                linea_examinada = grupo_asterisco[len(grupo_asterisco) - 1]
            linea_examinada = linea_examinada.replace('[',' ').replace(']',' ')
            linea_examinada = linea_examinada.split(' ')
            if linea_examinada[7] == '501001':
                total_grupos_A.append(grupo_asterisco)
            if linea_examinada[7] == '207002':
                total_grupos_B.append(grupo_asterisco)
            grupo_asterisco = []
    with open('./transacciones-2023_autA.txt', 'w') as archivoA:
        for grupo in total_grupos_A:
            for termino in grupo:
                archivoA.write(termino)
        archivoA.close()
    with open('./transacciones-2023_autB.txt', 'w') as archivoB:
        for grupo in total_grupos_B:
            for termino in grupo:
                archivoB.write(termino)
        archivoB.close()
    
    #En este caso, vamos enviar las cadenas de texto de tamaño SOCK_BUFFER a cada servidor
    #Usaremos la función definida al inicio para obtener los paquetes de tamaño SOCK_BUFFER
    Lista_arregloA = RetornaGruposSock('./transacciones-2023_autA.txt')
    ClienteA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClienteA.connect(('localhost',5001))
    print('Conexión establecida con la autorización A.')
    
    
    for cadena in Lista_arregloA:
        ClienteA.sendall(cadena.encode('utf-8'))
        while True:
            recibido = ClienteA.recv(SOCK_BUFFER)
            if recibido:
                break
    ClienteA.sendall('Terminado'.encode('utf-8'))
    print('Cerrando conexión desde servidor...')
    ClienteA.close()
    print('Conexión cerrada con la autorización A.')

    Lista_arregloB = RetornaGruposSock('./transacciones-2023_autB.txt')
    ClienteB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClienteB.connect(('localhost',5002))
    print('Conexión establecida con la autorización B.')
    
    
    for cadena in Lista_arregloB:
        ClienteB.sendall(cadena.encode('utf-8'))
        while True:
            recibido = ClienteB.recv(SOCK_BUFFER)
            if recibido:
                break
    ClienteB.sendall('Terminado'.encode('utf-8'))
    print('Cerrando conexión desde servidor...')
    ClienteB.close()
    print('Conexión cerrada con la autorización B.')
    