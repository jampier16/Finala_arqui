import requests
import concurrent.futures
import time
import statistics 

# URLs de las páginas a explorar
urls = [
    "https://www.wikipedia.org/",
    "https://www.nytimes.com/",
    "https://www.bbc.com/",
    "https://www.python.org/",
    "https://www.reddit.com/",
    "https://www.instagram.com/",
    "https://www.twitter.com/",
    "https://www.cnn.com/",
    "https://www.github.com/",
    "https://www.spotify.com/",
]

# Función para descargar el HTML de una URL y guardarlo en un archivo
def descargar_html(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            file.write(response.text)


if __name__=='__main__':

    # a) Descargar secuencialmente y medir el tiempo de ejecución
    tiempo_secuencial=[]
    for _ in range(5):
        inicio_secuencial = time.perf_counter()
        for i, url in enumerate(urls, start=1):
            nombre_archivo = f"pagina{i}.html"
            descargar_html(url, nombre_archivo)
        fin_secuencial = time.perf_counter()
        tiempo_secuencial.append(fin_secuencial - inicio_secuencial)
    print(f"Tiempo secuencial: {statistics.median(tiempo_secuencial)} segundos")
    
    # b) Descargar utilizando un Thread Pool con 3 workers y medir el tiempo de ejecución
    tiempo_pool=[]
    for _ in range(2):
        inicio_pool = time.perf_counter()
        num_workers=3
        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as ejecutor:
            for i, url in enumerate(urls, start=1):
                nombre_archivo = f"pagina{i}.html"
                ejecutor.submit(descargar_html, url, nombre_archivo)
        fin_pool = time.perf_counter()
        tiempo_pool.append(fin_pool - inicio_pool)

    print(f"Tiempo usando ThreadPool ({num_workers} workers): {statistics.median(tiempo_pool)} segundos")

    #c)
    # i) El speedup se debe la cantida de archivos html que se pueden descargar en simultaneo
    # En el caso secuencial se tiene que descargar uno por uno, pero en el caso asincrono de Pool de hilos, 
    # en particular con 3 workers, este puede descargar simultaneamente varios archivos html.
    # Las intrucciones beneficiadas es la  funcion descargar_html principlamente, y las variables 
    # relacionadas como los urls.

    #d)
    # No necesariemente aumentar el numero de worker disminuye el tiempo de ejecucion, en este caso 
    # se pude observar que a parti de 5 workers ya no disminuye el tiempo de ejecucion. Asi que para 
    # mas de 6 workers tiempo de ejecucion parece mantenerse. Tampo disminuye linealmnete.
    # Esto se debe a que el cpu tiene recusos limitados y a medida que se aumenta el numero de workers 
    # tambien se aumenta la carga en recursos. Por otra parte se hace mas complicada la gestion  de hilos,
    # por lo que herian falta mecanismos de de sincronizacion como bloqueos.
    


