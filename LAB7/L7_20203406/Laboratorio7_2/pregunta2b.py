import time
import matplotlib.pyplot as plt 
def pregunta2b(Codigo_alumno):
    n_archivos = 2
    cant_filas = 80000
    matches = []
    for i in range(1,n_archivos):
        ubicacion = './archivosCSV/' + 'archivo' + str(i) +'.csv'
        with open(ubicacion) as archivo:
            cantidad_matches = 0
            salida = []
            cantidad_matches = 0
            for k in range(cant_filas//8):
                for linea_i in range(8):
                    linea_extraida = archivo.readline(-1)
                    linea_extraida = linea_extraida.replace("\n","")
                    linea_extraida = linea_extraida.split(',')
                    salida.append(linea_extraida)

                for j in range(8):
                    linea_vertical = ''
                    for linea in salida:
                        linea_vertical += linea[j]
                    if (linea_vertical == Codigo_alumno):
                        cantidad_matches += 1
                print(k)
            matches.append(cantidad_matches)
            archivo.close()
    return matches

if __name__ == '__main__':
    eje_x = []
    for i in range(1,51,1):
        eje_x.append(i)
    tiempo_inicio = time.perf_counter()
    datos_histograma = pregunta2b('20203406')
    tiempo_fin = time.perf_counter()
    print("El tiempo que se demora la funcion2d es: ", tiempo_fin - tiempo_inicio, "segundos.")

    plt.bar(eje_x, datos_histograma)
    plt.title('n° de archivo vs matches')
    plt.xlabel('N Archivo')
    plt.ylabel('Matches')
    plt.savefig('hist2_b.png')
    #El tiempo b se demora más debido a que en a se lee linea por linea