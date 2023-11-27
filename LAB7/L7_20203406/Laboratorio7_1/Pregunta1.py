import time
def Funcion1A(N):
    inicio_lectura = time.perf_counter()
    #########################################
    with open("pacientes.csv",'r') as archivo_inicio:
        resultado = []
        i = 0
        while True:
            linea = archivo_inicio.readline()
            if (i < N + 1) & (i > 0):
                resultado.append(linea)
            if (i == N):
                break
            i = i + 1
    archivo_inicio.close()
    final_lectura = time.perf_counter()

    #Se guarda la lectura en resultado
    inicio_ordenar = time.perf_counter()
    #############################################
    lineas_separadas = []
    for linea_junta in resultado:
        lineas_separadas.append(linea_junta.split(','))
    ##################################################

    for i in range(0, len(lineas_separadas)):
        for j in range(i + 1, len(lineas_separadas)):
            if lineas_separadas[i][4] >= lineas_separadas[j][4]:
                lineas_separadas[i], lineas_separadas[j] = lineas_separadas[j], lineas_separadas[i]

    #Esto intercambiará los elementos en las posiciones i y j de la lista lineas_separadas
    #Para tener al menor antes que al mayor

    lineas_ordenadas = []
    for linea_separada in lineas_separadas:
        lineas_ordenadas.append(','.join(linea_separada))
    final_ordenar = time.perf_counter()
    #Se guarda las lineas ordenadas en lineas_ordenadas

    inicio_escritura = time.perf_counter()
    with open("pacientes_ordenado.csv",'w') as archivo_final:
        archivo_final.writelines(lineas_ordenadas)

    final_escritura = time.perf_counter()


    tiempo_lectura = final_lectura - inicio_lectura
    tiempo_escritura = final_escritura - inicio_escritura 
    tiempo_ordenar = final_ordenar - inicio_ordenar

    print("Para N = ",N,", el tiempo de lectura es", tiempo_lectura, "segundos, el de escritura es", tiempo_escritura, "segundos y de ordenar los pacientes fue", tiempo_ordenar, "segundos.")

if __name__ == '__main__':
    N = [500,2500,5000]
    for n in N:
        Funcion1A(n)