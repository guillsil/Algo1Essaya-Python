PARED = "#"
EMOGI_PARED = "\U0001F533"
CAJA = "$"
EMOGI_CAJA = "\U0001F5C4"
OBJETIVO = "."
EMOGI_OBEJTIVO = "\U0001F539"
JUGADOR = "@"
EMOGI_JUGADOR = "\U0001F9B9"
ESPACIO = " "
EMOGI_ESPACIO = "\U00002B1C"
EMOGI_OBJETIVO_CAJA = "*"
EMOGI_OBJETIVO_JUGADOR = "+"

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

import os


'''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador
    Ejemplo:

    # >>> crear_grilla([
        '#####',
        '#.$ #',
        '#@  #',
        '#####',
        
    ])
    '''
LISTA = ["#####", "#.$ #", "#@  #", "#####"]
LISTA2 = ["  #####$", "##$ $.#$", "#.@$  #$", "#   $.#$", "#.#    #", "# $.$:##", "#    $.#", "########"]
def crear_grilla(desc):
    #descompone una cadena en una lista de tuplas cuyo contenido representa la (col, fil) de un objeto
    paredes = []
    cajas = []
    jugador = []
    objetivos = []
    for j in range(len(desc)):
        #j es la fila
        for k in range(len(desc[j])):
            # k es la columna
            if desc[j][k] == "#":
                paredes.append((k,j))
            elif desc[j][k] == "$":
                cajas.append((k,j))
            elif desc[j][k] == "@":
                jugador.append((k,j))
            elif desc[j][k] == ".":
                objetivos.append((k,j))
            elif desc[j][k] == "*":
                cajas.append((k,j))
                objetivos.append((k,j))
            elif desc[j][k] == "+":
                jugador.append((k,j))
                objetivos.append((k,j))
    grilla = [paredes, cajas, jugador, objetivos, (int(len(desc[0])), int(len(desc)))]
    # grilla devuelve listas de tuplas con las coordenadas de las paredes, cajas, jugador y objetivos
    #tambien devuelve una tupla con la cantidad de columnas y filas de la grilla(dimension)
    return grilla
"""print(crear_grilla(LISTA))"""

def hay_objetivo_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en un objetivo.'''
    if (c,f) in grilla[2] and (c,f) in grilla[3]:
        return True

def hay_objetivo_caja(grilla, c, f):
    '''Devuelve True si hay una caja en un objetivo.'''
    if (c,f) in grilla[1] and (c,f) in grilla[3]:
        return True


def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla (col, fil)'''
    return grilla[4]
"""print(dimensiones(crear_grilla(LISTA2)))"""


def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return (c,f) in grilla[0]
"""print(hay_pared(crear_grilla(LISTA2), 0, 1))"""

def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return (c,f) in grilla[3]
"""print(hay_objetivo(crear_grilla(LISTA2), 1, 2))"""

def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return (c,f) in grilla[1]
"""print(hay_caja(crear_grilla(LISTA2), 3, 2))"""
def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return (c,f) in grilla[2]
"""print(hay_jugador(crear_grilla(LISTA2), 2, 2))"""

def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    valores = []
    for i in range(len(grilla[3])):
        if grilla[3][i] in grilla[1]:
            valores.append(True)
        else:
            valores.append(False)
    # valores es una lista de booleanos que indica si cada objetivo tiene una caja
    if False in valores:
        return False
    else:
        return True

def copia_profunda(lista):
    """Realiza una copia profunda de una lista con sus sublistas y develve la misma sin modificar la original"""
    copia = []
    for i in lista:
        copia.append(i[:])
    return copia
def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.
    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:
    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur
    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    # creo una copia de la grilla para no modificar la original
    grilla2 = copia_profunda(grilla)
    jugador = grilla2[2][0]
    movimiento = direccion
    if hay_pared(grilla2, jugador[0]+movimiento[0], jugador[1]+movimiento[1]):
        # si hay una pared en la direccion del movimiento, no se puede mover
        return grilla2
    elif hay_caja(grilla2, jugador[0]+movimiento[0], jugador[1]+movimiento[1]):
        if hay_pared(grilla2, jugador[0]+2*movimiento[0], jugador[1]+2*movimiento[1]):
            # si hay una pared en la direccion del movimiento, no se puede mover
            return grilla2
        elif hay_caja(grilla2, jugador[0]+2*movimiento[0], jugador[1]+2*movimiento[1]):
            # si hay una caja en la direccion del movimiento, no se puede mover
            return grilla2
        else:
            # si no hay nada en la direccion del movimiento, se puede mover
            grilla2[1].remove((jugador[0]+movimiento[0], jugador[1]+movimiento[1]))
            grilla2[1].append((jugador[0]+2*movimiento[0], jugador[1]+2*movimiento[1]))
            grilla2[2].remove(jugador)
            grilla2[2].append((jugador[0]+movimiento[0], jugador[1]+movimiento[1]))
            return grilla2

    else:
        # si no hay nada en la direccion del movimiento, se puede mover
        grilla2[2].remove(jugador)
        grilla2[2].append((jugador[0]+movimiento[0], jugador[1]+movimiento[1]))
        return grilla2




def cargar_terreno(grilla):
    '''Carga el terreno en la grilla.'''
    for i in range(grilla[4][0]):
        for j in range(grilla[4][1]):
            if hay_pared(grilla, j, i):
                print(EMOGI_PARED, end="")
            elif hay_objetivo(grilla, j, i):
                if hay_jugador(grilla, j, i):
                    print(EMOGI_JUGADOR, end="")
                elif hay_caja(grilla, j, i):
                    print(EMOGI_CAJA, end="")
                else:
                    print(EMOGI_OBEJTIVO, end="")
            elif hay_caja(grilla, j, i):
                print(EMOGI_CAJA, end="")
            elif hay_jugador(grilla, j, i):
                print(EMOGI_JUGADOR, end="")
            else:
                print(EMOGI_ESPACIO, end="")
        print()

def pedir_movimiento():
    '''Pide al usuario que ingrese un movimiento y devuelve la dirección
    correspondiente.
    '''
    while True:
        direccion = input("Ingrese una direccion: ")
        if direccion == "W" or direccion == "w":
            return NORTE
        elif direccion == "S" or direccion == "s":
            return SUR
        elif direccion == "A" or direccion == "a":
            return OESTE
        elif direccion == "D" or direccion == "d":
            return ESTE
        else:
            print("Direccion invalida, intente nuevamente")
            continue

"""def main():
    '''Función principal del programa.'''
    grilla = crear_grilla(LISTA2)
    while not juego_ganado(grilla):
        cargar_terreno(grilla)
        grilla = mover(grilla, pedir_movimiento())
    cargar_terreno(grilla)
    print("Ganaste!")
main()"""