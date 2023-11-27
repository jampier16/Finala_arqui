import time
from multiprocessing import Process


def encontrar_contraseña():
    vocales = 'AEIOU'
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    contrasena_correcta = ''
    
    for primera in vocales:
        for segunda in vocales:
            for tercera in letras:
                posible_contrasena = primera + segunda + tercera
                #print(f'Probando contraseña: {posible_contrasena}')
                
                if posible_contrasena == 'AAZ':  
                    print(f'Contraseña encontrada: {posible_contrasena}')
                    
                    return 

def buscar_contrasena(vocal):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for segunda in 'AEIOU':
        for tercera in letras:
            posible_contrasena = vocal + segunda + tercera
            #print(f'Probando contraseña: {posible_contrasena}')
            if posible_contrasena == 'AAZ':  
                print(f'Contraseña encontrada por el proceso {vocal}: {posible_contrasena}')
                return posible_contrasena

if __name__=="__main__":

# a) encontrar contraseña secuencialente por fuerza bruta 
    start_time = time.time() 
    encontrar_contraseña()
    end_time = time.time()
    print(f'Tiempo de ejecución: {end_time - start_time} segundos')

# b) encontrar contraseña paralelizada  por fuerza bruta 
    start_time1 = time.time()
    procesos = []

    vocales = 'AEIOU'
    for vocal in vocales:
        proceso = Process(target=buscar_contrasena, args=(vocal,))
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    end_time1 = time.time()
    print(f'Tiempo de ejecución total: {end_time1 - start_time1} segundos')

