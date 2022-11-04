import gamelib

PARED = "#"
CAJA = "$"
OBJETIVO = "."
JUGADOR = "@"
ESPACIO = " "
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"

ANCHO_CELDA = 64
ALTO_CELDA = 64

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)



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
    # borrar la ultima cadena si es toda vacia (si el nivel termina con una linea en blanco)
    if desc[-1] == " " * max_col:
        desc.pop()
    return desc

def leer_nivel(archivo_nivel, nivel):
    """Busca el nivel solicitado en el archivo de niveles y lo devuelve como una lista de strings, noce debe devolver
    una linea vacia al final"""
    nivel = nivel + 1
    archivo = open(archivo_nivel, "r")
    desc = []
    for linea in archivo:
        if linea.startswith("Level " + str(nivel)) :
            for linea in archivo:
                if linea.startswith("Level "):
                    return desc
                else:
                    if linea != "":
                        desc.append(linea.rstrip())
    archivo.close()
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
    #Devuelve True si hay una pared en la columna y fila (c, f).
    return (c,f) in grilla[0]

def hay_objetivo(grilla, c, f):
    #Devuelve True si hay un objetivo en la columna y fila (c, f).
    return (c,f) in grilla[3]

def hay_caja(grilla, c, f):
    #Devuelve True si hay una caja en la columna y fila (c, f).
    return (c,f) in grilla[1]

def hay_jugador(grilla, c, f):
    #Devuelve True si el jugador está en la columna y fila (c, f).
    return (c,f) in grilla[2]


def copia_profunda(lista):
    """Realiza una copia profunda de una lista con sus sublistas y develve la misma sin modificar la original"""
    copia = []
    for i in lista:
        copia.append(i[:])
    return copia


def mover(grilla, movimiento):
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


def juego_mostrar(grilla):
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero
    ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con usar las funciones
    draw_text y draw_rectangle/draw_line y gamelib.draw_image."""
    max_fil = grilla[4][1]
    max_col = hallar_max_columnas(grilla)
    #Dibujar las paredes
    for i in range(max_col):
        #i es la columna
        for j in range(max_fil):
            #j es la fila
            if hay_pared(grilla, i, j):
                gamelib.draw_image("img/ground.gif", ANCHO_CELDA * i, ALTO_CELDA * j)
                gamelib.draw_image("img/wall.gif",ANCHO_CELDA*i,ALTO_CELDA*j)

            elif hay_caja(grilla, i, j):
                gamelib.draw_image("img/ground.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
                gamelib.draw_image("img/box.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
            elif hay_objetivo(grilla, i, j):
                gamelib.draw_image("img/ground.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
                gamelib.draw_image("img/goal.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
                if hay_jugador(grilla, i, j):
                    gamelib.draw_image("img/player.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
            elif hay_jugador(grilla, i, j):
                gamelib.draw_image("img/ground.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
                gamelib.draw_image("img/player.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
            else:
                gamelib.draw_image("img/ground.gif",ANCHO_CELDA*i,ALTO_CELDA*j)
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

def reiniciar_nivel(nivel_actual):
    """Reinicia el nivel."""
    grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", nivel_actual)))
    return grilla
def cargar_teclas(archivo):
    """Recibe un archivo de teclas donde cada linea tiene la siguiente forma <Tecla> = <Accion>, se debera delvolver un
    diccionario con la accion como clave y la tecla como valor, tener en cuenta que varias teclas pueden tener la misma accion"""
    teclas = {}
    with open(archivo, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            linea = linea.split(" = ")
            #ignorar lineas vacias
            if linea[0] == "":
                continue
            #si hay teclas que hacen lo mismo se guardan en una lista
            if linea[1] in teclas:
                teclas[(linea[1])].append(linea[0])
            else:
                teclas[(linea[1])] = [linea[0]]
    return teclas



def actualizar_estado(grilla, tecla, nivel):
    """Actualiza el estado del juego, según la `tecla` presionada.
    Devuelve el nuevo estado del juego.
    """
    teclas = cargar_teclas("teclas.txt")
    for accion in teclas:
        if accion == "NORTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, (0, -1))
        elif accion == "SUR":
            if tecla in teclas[accion]:
                grilla = mover(grilla, (0, 1))
        elif accion == "ESTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, (1, 0))
        elif accion == "OESTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, (-1, 0))
        elif accion == "REINICIAR":
            if tecla in teclas[accion]:
                grilla = reiniciar_nivel(nivel)
        elif accion == "SALIR":
            if tecla in teclas[accion]:
                gamelib.quit()
        elif accion == "NEXT_LEVEL":
            if tecla in teclas[accion]:
                nivel += 1
                grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", nivel)))
                ancho_ventana, alto_ventana = refrescar_ventana(grilla, nivel)
                gamelib.resize(ancho_ventana, alto_ventana)
    return grilla, nivel

def refrescar_ventana(grilla, nivel):
    """Refresca la ventana del juego."""
    max_col = hallar_max_columnas(completar_grilla(leer_nivel("niveles.txt", nivel)))
    return max_col * ANCHO_CELDA, grilla[4][1] * ALTO_CELDA

