import gamelib
from soko import *
def juego_mostrar(grilla):
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero
    ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con usar las funciones
    draw_text y draw_rectangle/draw_line y gamelib.draw_image."""
    tamanio = dimencion_grilla(grilla)
    for i in range(tamanio[COL]):
        for j in range(tamanio[FIL]):
            if hay_pared(grilla, i, j):
                gamelib.draw_image("img/ground.gif", TAMANIO_CELDA * i, TAMANIO_CELDA* j)
                gamelib.draw_image("img/wall.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_caja(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/box.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_objetivo(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/goal.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                if hay_jugador(grilla, i, j):
                    gamelib.draw_image("img/player.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_jugador(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/player.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            else:
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)

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

def completar_grilla(desc):
    """Devuelve una lista de string complentando los espacios en blanco del final de cada
     string, teniendo en cuenta la cantidad de columnas maxima, también saca el nombre del nivel si lo continene y
     lo devuelve como string"""
    nombre = ""
    max_col = hallar_max_columnas(desc)
    for i in range(len(desc)):
        while len(desc[i]) < max_col:
            desc[i] += " "
    return desc
def obtener_nivel(archivo_nivel):
    """Lee el archivo de niveles y devuelve una lista con los niveles donde cada nivel es una lista de strings"""
    try:
        niveles = []
        with open(archivo_nivel) as archivo:
            desc = []
            for linea in archivo:
                if linea == "\n":
                    niveles.append(completar_grilla(desc))
                    desc = []
                else:
                    if  not linea.startswith("Level ") and not linea.startswith("'"):
                        desc.append(linea.rstrip())
            niveles.append(completar_grilla(desc))
        return niveles
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de niveles no existe")


def actualizar_estado(grilla, tecla, nivel, teclas, niveles):
    """Actualiza el estado del juego, según la `tecla` presionada.
    Devuelve el nuevo estado del juego.
    """
    #si la tecla no esta en el diccionario de teclas, no hacer nada
    if tecla not in teclas:
        return grilla, nivel
    #si la tecla esta en el diccionario de teclas, ejecutar la accion correspondiente
    if teclas[tecla] == "OESTE":
        grilla = mover(grilla, OESTE)
    elif teclas[tecla] == "ESTE":
        grilla = mover(grilla, ESTE)
    elif teclas[tecla] == "NORTE":
        grilla = mover(grilla, NORTE)
    elif teclas[tecla] == "SUR":
        grilla = mover(grilla, SUR)
    elif teclas[tecla] == "REINICIAR":
        grilla = crear_grilla(niveles[nivel])
    elif teclas[tecla] == "NEXT_LEVEL":
        if nivel < MAX_LEVEL:
            nivel += 1
            grilla = crear_grilla(niveles[nivel])
    elif teclas[tecla] == "PREV_LEVEL":
        if nivel > 0:
            nivel -= 1
            grilla = crear_grilla(niveles[nivel])
    return grilla, nivel

def cargar_teclas(archivo):
    """Recibe un archivo de teclas donde cada linea tiene la siguiente forma <Tecla> = <Accion>, se debera delvolver un
    diccionario con la TECLA como clave y la ACCION como valor"""
    try:
        teclas = {}
        with open(archivo) as archivo:
            for linea in archivo:
                linea = linea.strip().split(" = ")
                if linea[0] == "":
                    continue
                teclas[linea[0]] = linea[1]
        return teclas
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de teclas no existe")

def main():
    # Inicializar el estado del juego

    nivel = 153
    niveles = obtener_nivel("niveles.txt")
    grilla = crear_grilla(niveles[nivel])
    tamanio = dimencion_grilla(grilla)
    teclas_validas = cargar_teclas("teclas.txt")

    gamelib.resize(tamanio[COL] * TAMANIO_CELDA, tamanio[FIL] * TAMANIO_CELDA)


    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(grilla)
        gamelib.draw_end()

        gamelib.title("Sokoban++ - Nivel {}".format(nivel + 1))

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        grilla, nivel = actualizar_estado(grilla, tecla, nivel, teclas_validas, niveles)
        tamanio = dimencion_grilla(grilla)
        gamelib.resize(tamanio[COL] * TAMANIO_CELDA, tamanio[FIL] * TAMANIO_CELDA)

        # Verificar si el jugador ganó o perdió
        if juego_ganado(grilla):
            nivel += 1
            grilla = crear_grilla(niveles[nivel])
            tamanio = dimencion_grilla(grilla)
            gamelib.resize(tamanio[COL] * TAMANIO_CELDA, tamanio[FIL] * TAMANIO_CELDA)
        if nivel > MAX_LEVEL:
            gamelib.alert("GANASTE")
            break
gamelib.init(main)