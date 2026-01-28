
import random

def jugador():
    respuesta = input('\n ¿Qué jugada eliges (1: Piedra, 2: Papel, 3: Tijera)?: ')
    return int(respuesta)

def ordenador():
    opciones = ['piedra','papel','tijera']
    opcion = random.choice(opciones)
    return(opcion)

def compara(jugador,ordenador):
    ganador = None
    if (jugador == 1 and ordenador == 'tijera'): ganador = 'jugador'
    elif (jugador == 1 and ordenador == 'papel'): ganador = 'ordenador'
    elif (jugador == 1 and ordenador == 'piedra'): ganador = 'empate'
    elif (jugador == 2 and ordenador == 'tijera'): ganador = 'ordenador'
    elif (jugador == 2 and ordenador == 'papel'): ganador = 'empate'
    elif (jugador == 2 and ordenador == 'piedra'): ganador = 'jugador'
    elif (jugador == 3 and ordenador == 'tijera'): ganador = 'empate'
    elif (jugador == 3 and ordenador == 'papel'): ganador = 'jugador'
    elif (jugador == 3 and ordenador == 'piedra'): ganador = 'ordenador'
    else: print('Ha habido algún error')
    return(ganador)

if __name__ == "__main__":
    nombre = input('Cómo te llamas?: ')
    print('Hola %s vamos a echar 10 jugadas. Y el que consiga más puntos gana!' %nombre)

    puntos_j = 0
    puntos_o = 0

    for cada in range(10):
        tirada_jugador = jugador()
        tirada_ordenador = ordenador()
        ganador = compara(tirada_jugador,tirada_ordenador)
        if ganador == 'jugador':
            print('\n Yo he sacado %s'%tirada_ordenador)
            print('\n Así que esta la has ganado tú!!')
            puntos_j += 1
        elif ganador == 'ordenador':
            print('\n Yo he sacado %s'%tirada_ordenador)
            print('\n Así que esta la he ganado yo!!')
            puntos_o += 1
        elif ganador == 'empate':
            print('\n Vaya, yo también he sacado %s'%tirada_ordenador)
            print('\n Así que hemos empatado, venga otra mano')
        else: print('Ha habido algún problema')

    if puntos_j > puntos_o:
        puntos_finales = puntos_j
        print('\n HEMOS TERMINADO!!')
        print('\n El resultado final es que has ganado tú con {} puntos'.format(puntos_finales))
    elif puntos_j < puntos_o:
        puntos_finales = puntos_o
        print('\n El resultado final es que he ganado yo con {} puntos'.format(puntos_finales))
    else:
        print('\n Pues parece que hemos empatado, así que todos ganamos!')
