import gamelib

PARED = "#"
CAJA = "$"
OBJETIVO = "."
JUGADOR = "@"
ESPACIO = " "
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"

#OBJETOS DE CREAR GRILLA
PAREDES = 0
CAJAS = 1
JUGADOR_ = 2
OBJETIVOS = 3
TUPLA_DIMENCION = 4

COL = 0
FIL = 1
CORRIMIENTO = 2

OBJETOS_DEL_JUEGO = [PARED, CAJA, JUGADOR, OBJETIVO, OBJETIVO_CAJA, OBJETIVO_JUGADOR, ESPACIO]

GROSOR_CELDA = 64

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

MAX_LEVEL = 154

def dimencion_grilla(grilla):
    """Devuelve la dimencion de la grilla"""
    return grilla[TUPLA_DIMENCION]


""""Esta funcion la puse aqui ya que crear grilla que pertenece a la logica del juego la necesita, pero no la puedo importar"""
def hallar_max_columnas(desc):
    """Devuelve el largo del string más largo, si el string no tiene una Pared, Caja, Jugador
    o Objetivo, se ignora y se sigue buscando"""
    max_col = 0
    for i in range(len(desc)):
        if desc[i] != "":
            if desc[i][0] in OBJETOS_DEL_JUEGO:
                if len(desc[i]) > max_col:
                    max_col = len(desc[i])
    return max_col

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
    #Devuelve True si hay una pared en la columna y fila (c, f).
    return (c,f) in grilla[PAREDES]

def hay_objetivo(grilla, c, f):
    #Devuelve True si hay un objetivo en la columna y fila (c, f).
    return (c,f) in grilla[OBJETIVOS]

def hay_caja(grilla, c, f):
    #Devuelve True si hay una caja en la columna y fila (c, f).
    return (c,f) in grilla[CAJAS]

def hay_jugador(grilla, c, f):
    #Devuelve True si el jugador está en la columna y fila (c, f).
    return (c,f) in grilla[JUGADOR_]


def copia_profunda(lista):
    """Realiza una copia profunda de una lista con sus sublistas y develve la misma sin modificar la original"""
    copia = []
    for i in lista:
        copia.append(i[:])
    return copia


def mover(grilla, movimiento):
    ''' Mueve el jugador en la dirección indicada.
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
    jugador = grilla2[JUGADOR_][COL]
    if hay_pared(grilla2, jugador[COL]+movimiento[COL], jugador[FIL]+movimiento[FIL]):
        # si hay una pared en la direccion del movimiento, no se puede mover
        return grilla2
    elif hay_caja(grilla2, jugador[COL]+movimiento[COL], jugador[FIL]+movimiento[FIL]):
        if hay_pared(grilla2, jugador[COL]+CORRIMIENTO*movimiento[COL], jugador[FIL]+CORRIMIENTO*movimiento[FIL]):
            # si hay una pared en la direccion del movimiento, no se puede mover
            return grilla2
        elif hay_caja(grilla2, jugador[COL]+CORRIMIENTO*movimiento[COL], jugador[FIL]+CORRIMIENTO*movimiento[FIL]):
            # si hay una caja en la direccion del movimiento, no se puede mover
            return grilla2
        else:
            # si no hay nada en la direccion del movimiento, se puede mover
            grilla2[CAJAS].remove((jugador[COL]+movimiento[COL], jugador[FIL]+movimiento[FIL]))
            grilla2[CAJAS].append((jugador[COL]+CORRIMIENTO*movimiento[COL], jugador[FIL]+CORRIMIENTO*movimiento[FIL]))
            grilla2[JUGADOR_].remove(jugador)
            grilla2[JUGADOR_].append((jugador[COL]+movimiento[COL], jugador[FIL]+movimiento[FIL]))
            return grilla2

    else:
        # si no hay nada en la direccion del movimiento, se puede mover
        grilla2[JUGADOR_].remove(jugador)
        grilla2[JUGADOR_].append((jugador[COL]+movimiento[COL], jugador[FIL]+movimiento[FIL]))
        return grilla2


def juego_mostrar(grilla):
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero
    ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con usar las funciones
    draw_text y draw_rectangle/draw_line y gamelib.draw_image."""
    tamanio = dimencion_grilla(grilla)
    for i in range(tamanio[COL]):
        for j in range(tamanio[FIL]):
            if hay_pared(grilla, i, j):
                gamelib.draw_image("img/ground.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
                gamelib.draw_image("img/wall.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
            elif hay_caja(grilla, i, j):
                gamelib.draw_image("img/ground.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
                gamelib.draw_image("img/box.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
            elif hay_objetivo(grilla, i, j):
                gamelib.draw_image("img/ground.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
                gamelib.draw_image("img/goal.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
                if hay_jugador(grilla, i, j):
                    gamelib.draw_image("img/player.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
            elif hay_jugador(grilla, i, j):
                gamelib.draw_image("img/ground.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
                gamelib.draw_image("img/player.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)
            else:
                gamelib.draw_image("img/ground.gif", GROSOR_CELDA * i, GROSOR_CELDA * j)



def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    valores = []
    for i in range(len(grilla[OBJETIVOS])):
        if grilla[OBJETIVOS][i] in grilla[CAJAS]:
            valores.append(True)
        else:
            valores.append(False)
    # valores es una lista de booleanos que indica si cada objetivo tiene una caja
    if False in valores:
        return False
    else:
        return True





