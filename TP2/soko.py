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
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"

LISTA_DE_SIMBOLOS = [PARED, CAJA, JUGADOR, OBJETIVO, ESPACIO, EMOGI_PARED, EMOGI_CAJA, EMOGI_JUGADOR, EMOGI_OBEJTIVO, EMOGI_ESPACIO, OBJETIVO_CAJA, OBJETIVO_JUGADOR]
OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

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
def grilla_a_diccionario(grilla):
    """"devuelve un diccionario donde la clave es la posicion de cada elemento y el valor es el simbolo que representa"""
    diccionario = {}
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            diccionario[grilla[i][j]] = LISTA_DE_SIMBOLOS[i]
    return diccionario


def imprimir_grilla(grilla):
    """Imprime la grilla"""
    diccionario = grilla_a_diccionario(grilla)
    for i in range(grilla[4][1]):
        for j in range(grilla[4][0]):
            if (j,i) in diccionario:
                print(diccionario[(j,i)], end="")
            else:
                print(" ", end="")
        print()
def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla (col, fil)'''
    return grilla[4]
"""print(dimensiones(crear_grilla(LISTA2)))"""

def hallar_max_columnas(desc):
    """Devuelve la maxima cantidad de columnas de la desc"""
    max_col = 0
    for i in range(len(desc)):
        if len(desc[i]) > max_col:
            max_col = len(desc[i])
    return max_col

def completar_grilla(desc):
    """Recibe una lista de string y devuelve una lista de string complentando los espacios en blanco del final de cada
     string, teniendo en cuenta la cantidad de columnas maxima"""
    max_col = hallar_max_columnas(desc)
    for i in range(len(desc)):
        while len(desc[i]) < max_col:
            desc[i] = desc[i] + " "
    return desc

def leer_nivel(archivo_nivel, nivel):
    """Busca el nivel solicitado en el archivo de niveles y lo devuelve como una lista de strings"""
    nivel = nivel + 1
    archivo = open(archivo_nivel, "r")
    desc = []
    for linea in archivo:
        if linea.startswith("Level " + str(nivel)):
            for linea in archivo:
                if linea.startswith("Level "):
                    return desc
                else:
                    if linea != "":
                        desc.append(linea.rstrip())
    #borrar el ultimo elemento de la lista
    desc.pop()
    return desc

def crear_grilla(desc):
    """Crea una grilla a partir de la descripcion del estado inicial"""
    paredes = []
    cajas = []
    jugador = []
    objetivos = []
    vacios = []
    max_col = hallar_max_columnas(desc)
    for j in range(len(desc)):
        for k in range(max_col):
            if desc[j][k] == PARED:
                paredes.append((k, j))
            elif desc[j][k] == CAJA:
                cajas.append((k, j))
            elif desc[j][k] == JUGADOR:
                jugador.append((k, j))
            elif desc[j][k] == OBJETIVO:
                objetivos.append((k, j))
            elif desc[j][k] == OBJETIVO_CAJA:
                cajas.append((k, j))
                objetivos.append((k, j))
            elif desc[j][k] == OBJETIVO_JUGADOR:
                jugador.append((k, j))
                objetivos.append((k, j))
            else:
                vacios.append((k, j))
    return paredes, cajas, jugador, objetivos, (max_col, len(desc))


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
def cargar_terreno(dic_grilla):
    """Carga el terreno en la grilla."""

    for i in range(grilla[4][0]+1):
        for j in range(grilla[4][1]-2):
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

print(leer_nivel("niveles.txt", 154))
print(completar_grilla(leer_nivel("niveles.txt", 154)))
grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", 154)))
print(grilla_a_diccionario(grilla))
imprimir_grilla(grilla)


"""def main():
    '''Función principal del programa.'''
    grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", 2)))
    while not juego_ganado(grilla):
        cargar_terreno(grilla)
        grilla = mover(grilla, pedir_movimiento())
    cargar_terreno(grilla)
    print("Ganaste!")
main()"""