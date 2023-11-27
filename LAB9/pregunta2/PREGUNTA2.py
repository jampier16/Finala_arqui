import random
import asyncio
import aiofiles 
import time 

ganador_rondas= ""
puntajes=[0]*8
puntajes_async=[0]*8

#a) Lectura del archivo players 
with open('./players.csv','r') as archi:
    lineas = archi.readlines()
    nombres=[]
    ratings=[]
    for linea in lineas[1:len(lineas)]:
        nombres.append(linea.split(';')[0])
        ratings.append((linea.split(';')[1].replace('\n','')))

#b)Fase rondas  - Asincrono
async def partida_async(jugador1, jugador2):

    posicion1= nombres.index(jugador1)
    rating1= ratings[posicion1]
    posicion2= nombres.index(jugador2)
    rating2= ratings[posicion2]
    
    if(rating1>rating2):
        puntajes_async[posicion1]+=1
    else:
        puntajes_async[posicion2]+=1
    await asyncio.sleep(0.15) 

async def fase_rodas_async():

    print("Ronda 1 - Dia 1") 
    await asyncio.gather(partida_async("Levon Aronian" , "Magnus Carlsen"),
                         partida_async("Boris Gelfand" , "Alexander Grischuk"),
                         partida_async("Peter Svidler", "Vladimir Kramnik"))

    print("Ronda 2 - Dia 2") 
    await asyncio.gather(partida_async("Magnus Carlsen" , "Vladimir Kramnik"),
                         partida_async("Alexander Grischuk" , "Peter Svidler"),
                         partida_async("Levon Aronian", "Boris Gelfand"))
    
    print("Ronda 3 - Dia 3") 
    await asyncio.gather(partida_async("Boris Gelfand" , "Magnus Carlsen"),
                         partida_async("Peter Svidler" , "Levon Aronian"),
                         partida_async("Vladimir Kramnik", "Alexander Grischuk"))
    print("Ronda 4 - Dia 4") 
    await asyncio.gather(partida_async("Magnus Carlsen" , "Alexander Grischuk"),
                         partida_async("Peter Svidler" , "Vladimir Kramnik"),
                         partida_async("Boris Gelfand", "Peter Svidler"))

    print("Ronda 5 - Dia 5") 
    await asyncio.gather(partida_async("Peter Svidler" , "Magnus Carlsen"),
                         partida_async("Vladimir Kramnik" , "Boris Gelfand"),
                         partida_async("Alexander Grischuk", "Levon Aronian"))
    ganador = max(puntajes_async, key=lambda x: x)
    posicion_ganador=puntajes_async.index(ganador)
    print(f"el ganador de la primera fase es: {nombres[posicion_ganador]}, con un puntaje de: {puntajes_async[posicion_ganador]}")

#c) Fase rondas - Sincrono 
def partida_sync(jugador1, jugador2):
        posicion1= nombres.index(jugador1)
        rating1= ratings[posicion1]
        posicion2= nombres.index(jugador2)
        rating2= ratings[posicion2]
        
        if(rating1>rating2):
            puntajes[posicion1]+=1
        else:
            puntajes[posicion2]+=1
        time.sleep(0.15) 

def fase_rodas_sync():
    global ganador_rondas 
    print("Ronda 1 - Dia 1") 
    partida_sync("Levon Aronian" , "Magnus Carlsen"),
    partida_sync("Boris Gelfand" , "Alexander Grischuk"),
    partida_sync("Peter Svidler", "Vladimir Kramnik")

    print("Ronda 2 - Dia 2") 
    partida_sync("Magnus Carlsen" , "Vladimir Kramnik"),
    partida_sync("Alexander Grischuk" , "Peter Svidler"),
    partida_sync("Levon Aronian", "Boris Gelfand")
    
    print("Ronda 3 - Dia 3") 
    partida_sync("Boris Gelfand" , "Magnus Carlsen"),
    partida_sync("Peter Svidler" , "Levon Aronian"),
    partida_sync("Vladimir Kramnik", "Alexander Grischuk")

    print("Ronda 4 - Dia 4") 
    partida_sync("Magnus Carlsen" , "Alexander Grischuk"),
    partida_sync("Peter Svidler" , "Vladimir Kramnik"),
    partida_sync("Boris Gelfand", "Peter Svidler")

    print("Ronda 5 - Dia 5") 
    partida_sync("Peter Svidler" , "Magnus Carlsen"),
    partida_sync("Vladimir Kramnik" , "Boris Gelfand"),
    partida_sync("Alexander Grischuk", "Levon Aronian")

    puntaje_ganador = max(puntajes, key=lambda x: x)
    posicion_ganador=puntajes.index(puntaje_ganador)
    ganador_rondas= nombres[posicion_ganador]
    print(f"El ganador de la primera fase es: {ganador_rondas}, con un puntaje de: {puntaje_ganador}\n")

#d) Fase Final - Sincrona 
#nota: Se require saber quien es el ganador de rondas para saber el ganador dle torneo
def fase_final():
    for i in range(12):
        puntaje_ganador_rondas=0
        puntaje_anand=0
        ganador=""
        rating_ganador_rondas=random.randint(2000, 3000)
        rating_anand= random.randint(2000, 3000)
        if(rating_ganador_rondas>rating_anand):
            puntaje_ganador_rondas+=1
        else:
            puntaje_anand+=1
    if(puntaje_ganador_rondas>puntaje_anand):
        ganador=ganador_rondas         
    else:
        ganador= "Anand"
    print(f"El ganador del tornedo de ajedrez es: {ganador}")

if __name__=="__main__":
    asyncio.run(fase_rodas_async()) 
    fase_rodas_sync()
    fase_final()