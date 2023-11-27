import random
import asyncio
import aiofiles 


puntajes=[0]*8
#a) lectura del archivo players 
with open('./players.csv','r') as archi:
    lineas = archi.readlines()
    nombres=[]
    ratings=[]
    for linea in lineas[1:len(lineas)]:
        nombres.append(linea.split(';')[0])
        ratings.append((linea.split(';')[1].replace('\n','')))

#b)Fase rondas  - Asincrono
async def partida(jugador1, jugador2):
    posicion1= nombres.index(jugador1)
    rating1= ratings[posicion1]
    print(posicion1, rating1)
    posicion2= nombres.index(jugador2)
    rating2= ratings[posicion2]
    print(posicion2, rating2)
    
    if(rating1>rating2):
        puntajes[posicion1]+=1
    else:
        puntajes[posicion2]+=1
    await asyncio.sleep(0.15) 

async def fase_rodas():
    print("Ronda 1 - Dia 1") 
    await asyncio.gather(partida("Levon Aronian" , "Magnus Carlsen"),
                         partida("Boris Gelfand" , "Alexander Grischuk"),
                         partida("Peter Svidler", "Vladimir Kramnik"))

    print("Ronda 2 - Dia 2") 
    await asyncio.gather(partida("Magnus Carlsen" , "Vladimir Kramnik"),
                         partida("Alexander Grischuk" , "Peter Svidler"),
                         partida("Levon Aronian", "Boris Gelfand"))
    
    print("Ronda 3 - Dia 3") 
    await asyncio.gather(partida("Boris Gelfand" , "Magnus Carlsen"),
                         partida("Peter Svidler" , "Levon Aronian"),
                         partida("Vladimir Kramnik", "Alexander Grischuk"))
    print("Ronda 4 - Dia 4") 
    await asyncio.gather(partida("Magnus Carlsen" , "Alexander Grischuk"),
                         partida("Peter Svidler" , "Vladimir Kramnik"),
                         partida("Boris Gelfand", "Peter Svidler"))

    print("Ronda 5 - Dia 5") 
    await asyncio.gather(partida("Peter Svidler" , "Magnus Carlsen"),
                         partida("Vladimir Kramnik" , "Boris Gelfand"),
                         partida("Alexander Grischuk", "Levon Aronian"))
    ganador = max(puntajes, key=lambda x: x)
    posicion_ganador=puntajes.index(ganador)
    print(f"el ganador de la primera fase es: {nombres[posicion_ganador]}, con un puntaje de: {puntajes[posicion_ganador]}")

#c) Fase rondas - Sincrono 

if __name__=="__main__":
    asyncio.run(fase_rodas()) 
