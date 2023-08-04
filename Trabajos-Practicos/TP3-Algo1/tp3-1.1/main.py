from pila import Pila
from cola import Cola
from soko import *

def leer_nivel(archivo_nivel, nivel):
    """Busca el nivel solicitado en el archivo de niveles y lo devuelve como una lista de strings, no se debe devolver
    una línea vaciá al final"""
    try:
        nivel = nivel + 1
        desc = []
        with open(archivo_nivel) as archivo:
            # si el archivo esta vacio lanzar una excepcion
            if archivo.read() == "":
                raise ValueError("El archivo de niveles esta vacio")
            archivo.seek(0)
            for linea in archivo:
                if linea.startswith("Level " + str(nivel)):
                    for linea in archivo:
                        if linea.startswith("Level "):
                            return desc
                        else:
                            if linea != "":
                                desc.append(linea.rstrip())
            return desc
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de niveles no existe")

def reiniciar_nivel(nivel_actual, niveles):
    """Reinicia el nivel."""
    niveles = lista_niveles()
    grilla = niveles[nivel_actual]
    return grilla



def actualizar_estado(grilla, tecla, nivel, teclas, niveles):
    """Actualiza el estado del juego, según la `tecla` presionada.
    Devuelve el nuevo estado del juego.
    """
    """Implementar las funcionalidades de deshacer y rehacer, usando la tecla 'z' para deshacer y 'y' para rehacer, 
    y dos pilas para guardar los estados del juego"""
    pila_hacer = Pila()
    pila_rehacer_deshacer = Pila()

    tamanio = dimencion_grilla(grilla)
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
        grilla = reiniciar_nivel(nivel, niveles)
    elif teclas[tecla] == "NEXT_LEVEL":
        nivel += 1
        grilla = reiniciar_nivel(nivel, niveles)
        tamanio = dimencion_grilla(grilla)
        gamelib.resize(tamanio[COL] * GROSOR_CELDA, tamanio[FIL] * GROSOR_CELDA)
    elif teclas[tecla] == "PREV_LEVEL":
        nivel -= 1
        grilla = reiniciar_nivel(nivel, niveles)
        tamanio = dimencion_grilla(grilla)
        gamelib.resize(tamanio[COL] * GROSOR_CELDA, tamanio[FIL] * GROSOR_CELDA)



    return grilla, nivel

def cargar_teclas(archivo):
    """Recibe un archivo de teclas donde cada linea tiene la siguiente forma <Tecla> = <Accion>, se debera delvolver un
    diccionario con la TECLA como clave y la ACCION como valor"""
    try:
        teclas = {}
        with open(archivo) as archivo:
            # si el archivo esta vacio o no existen lanzar una excepcion
            if archivo.read() == "":
                raise ValueError("El archivo de teclas esta vacio")
            archivo.seek(0)
            for linea in archivo:
                linea = linea.strip().split(" = ")  # separar la linea en dos partes
                # ignorar lineas vacias
                if linea[0] == "":
                    continue
                teclas[linea[0]] = linea[1]
        return teclas
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de teclas no existe")

def completar_grilla(desc):
    """Devuelve una lista de string complentando los espacios en blanco del final de cada
     string, teniendo en cuenta la cantidad de columnas maxima, también saca el nombre del nivel si lo continene y
     lo devuelve como string"""
    max_col = hallar_max_columnas(desc)
    for i in range(len(desc)):
        while len(desc[i]) < max_col:
            desc[i] = desc[i] + " "
    #si la primera linea no continene objetos del nivel , es el nombre del nivel por lo tanto se debera
    # eliminar y devolver como un string
    if desc[0].startswith("'"):
        name_level = desc[0]
        desc.pop(0)
    else:
        name_level = ""
    # borrar la última cadena si es toda vacia (si el nivel termina con una linea en blanco)
    if desc[-1] == " " * max_col:
        desc.pop()
    return desc, name_level

def lista_niveles():
    """Devuelve una lista de tuplas con todos los niveles del juego"""
    lista = []
    for i in range(MAX_LEVEL):
        #agregar los niveles
        lista.append((crear_grilla(completar_grilla(leer_nivel("niveles.txt", i))[0])))
    return lista
def nombre_de_niveles():
    """Devuelve una lista con todos los nombres de los niveles del juego"""
    lista = []
    for i in range(MAX_LEVEL):
        #agregar los niveles
        lista.append(completar_grilla(leer_nivel("niveles.txt", i))[1])
    return lista

#Backtracking
"""Pistas
Presionando una tecla determinada (configurable mediante teclas.txt), el efecto dependerá de dos casos posibles:
    No hay pistas disponibles: en este caso el juego intentará encontrar una solución al nivel, 
    utilizando el algoritmo de backtracking que se describe a continuación. Si se encuentra la solución, 
    la sucesión de acciones correspondiente será considerada como las pistas disponibles.

    Hay pistas disponibles: Se desencola una pista y se efectúa esa acción, como si la hubiera hecho el jugador.

Si el jugador efectúa cualquier otra acción que no sea la acción de "pista", se debe descartar las pistas 
disponibles, ya que no podemos asegurar que sean válidas para el estado actual."""
"""Backtracking es un método para encontrar todas las soluciones (o algunas) a problemas computacionales, que 
consiste en plantear soluciones candidatas e ir descartando (backtrack) las que se determina que no son 
soluciones.
Para resolver un nivel de Sokoban utilizando backtracking, lo más fácil es plantear el algoritmo en forma
 recursiva:"""






def main():
    # Inicializar el estado del juego
    nivel = 0
    niveles = lista_niveles()
    grilla = niveles[nivel]
    tamanio = dimencion_grilla(grilla)
    teclas_validas = cargar_teclas("teclas.txt")
    movimiento_solucion = Cola()
    movimiento = Pila()
    deshacer_rehacer = Pila()
    """Deshacer y rehacer
    Presionando una tecla determinada (configurable mediante teclas.txt), el efecto dependerá de dos casos posibles:
    No hay acciones deshechas: en este caso se debe guardar el estado actual del juego, para poder deshacerlo
    posteriormente.
    
    Hay acciones deshechas: se debe deshacer la última acción realizada por el jugador, y se debe guardar el
    estado actual del juego, para poder rehacerlo posteriormente."""

    gamelib.resize(tamanio[COL] * GROSOR_CELDA, tamanio[FIL] * GROSOR_CELDA)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(grilla)
        # cambiar texto de la ventana
        name_level = nombre_de_niveles()[nivel]
        gamelib.title("Sokoban++ - Nivel {} - {}".format(nivel + 1, name_level))
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        if tecla in teclas_validas:
            if teclas_validas[tecla] == "DESHACER":
                if deshacer_rehacer.esta_vacia():
                    grilla = deshacer_rehacer.desapilar()
                else:
                    grilla = deshacer_rehacer.desapilar()

            else:
                grilla, nivel = actualizar_estado(grilla, tecla, nivel, teclas_validas, niveles)
                deshacer_rehacer.apilar(grilla)
        """grilla, nivel = actualizar_estado(grilla, tecla, nivel, teclas_validas, niveles)"""

        # Verificar si el jugador ganó o perdió
        if juego_ganado(grilla):
            nivel += 1
            grilla = lista_niveles()[nivel]
            gamelib.resize(tamanio[COL] * GROSOR_CELDA, tamanio[FIL] * GROSOR_CELDA)
            name_level = nombre_de_niveles()[nivel]
        if nivel == MAX_LEVEL:
            gamelib.alert("GANASTE")
            break

gamelib.init(main)