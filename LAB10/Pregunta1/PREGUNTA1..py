from urllib.request import urlopen 
import time 
import statistics
from threading import Thread

url1= 'https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/'
def descargar_arhivo(i): #descargar un archivo 
    global url 
    url2=""
    url=""
    if i <= 9:
        url2 += '0' + str(i)+'.png'   
    else: 
        url2 += str(i)+'.png'
    url= url1+url2
    with urlopen(url) as page:
        image_data = page.read()
    with open('pato_'+url2, 'wb') as archivo:
        archivo.write(image_data)
    url2=""
    url=""
        
if __name__=='__main__':
    #a)
    tem1=[]
    for i in range(5):
        tem1i= time.perf_counter()
        for i in range(1,30):
            descargar_arhivo(i)
        tem1f= time.perf_counter()
        tem1.append(tem1f- tem1i)
    print(f'El tiempo promedio en la descarga secuencial: {statistics.median(tem1)} segundos.')
    #b)
    tem2=[]
    for i in range(5):
        tem2i= time.perf_counter()
        for i in range(1,30):
            t = Thread(target=descargar_arhivo(i))
            t.start()       
        tem2f = time.perf_counter()
        tem2.append(tem2f- tem2i)
    print(f'El tiempo promedio en la descarga por mutihilos: {statistics.median(tem1)} segundos.')
    #c)
    tem3=[]
    for i in range(5):
        tem3i= time.perf_counter()
        for i in range(1,30):
            t1 = Thread(target=descargar_arhivo(i))
            t1.start()       
            if(i%3):
                t1.join() #esto limita el numero de hilos concurrentes a 3
        tem3f= time.perf_counter()
        tem3.append(tem3f- tem3i)
    print(f'El tiempo promedio en la descarga por 3 hilos: {statistics.median(tem3)} segundos.')




