import time
import matplotlib.pyplot as plt 

def pregunta2d(Codigo_Alumno):
    n_archivos = 51
    n_filas = 80000
    n_intervalos = 500
    matches = []
    for i in range(1,n_archivos):
        ubicacion = './archivosCSV/' + 'archivo' + str(i) +'.csv'
        with open(ubicacion) as archivo:
            cantidad_matches = 0
            for j in range(n_filas//n_intervalos):
                grupo500 = []
                for k in range(n_intervalos):
                    linea_extraida = archivo.readline(-1)
                    linea_extraida = linea_extraida.replace("\n","")
                    linea_extraida = linea_extraida.replace(",","")
                    grupo500.append(linea_extraida)
                for linea500 in grupo500:
                    if (linea500 == Codigo_Alumno):
                        cantidad_matches += 1
            matches.append(cantidad_matches)
            archivo.close()
    return matches
if __name__ == '__main__':
    tiempo_inicio = time.perf_counter()
    print(pregunta2d('20203406'))
    tiempo_fin = time.perf_counter()
    print("El tiempo que se demora la funcion2d es: ", tiempo_fin - tiempo_inicio, "segundos.")

    #El tiempo a sigue permaneciendo mayor
    