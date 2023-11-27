import matplotlib.pyplot as plt 
import time
def funcion2a(Codigo_alumno):
    n_archivos = 51
    matches = []
    for i in range(1,n_archivos): # itera sobre la cantidad de archivos 
        ubicacion = './archivosCSV/' + 'archivo' + str(i) +'.csv'
        with open(ubicacion) as archivo:
            cantidad_matches = 0
            lista = archivo.readlines()
            for linea in lista: 
                linea = linea.replace(",","")
                linea = linea.replace("\n","")
                if (linea == Codigo_alumno):
                    cantidad_matches += 1
            matches.append(cantidad_matches)
            archivo.close()
    return matches
if __name__ == '__main__':
    ###############
    eje_x = []
    for i in range(1,51,1):
        eje_x.append(i)
    #####################
    #alt: list(range(1,51))

    tiempo_inicio = time.perf_counter()
    datos_histograma = funcion2a('43991123')
    print(datos_histograma)
    tiempo_final= time.perf_counter()
    print("El tiempo que se demora la funcion2a es: ", tiempo_final - tiempo_inicio, "segundos.")

    plt.bar(eje_x, datos_histograma)
    plt.title('n° de archivo vs matches')
    plt.xlabel('N Archivo')
    plt.ylabel('Matches')
    plt.savefig('hist2_a.png')

