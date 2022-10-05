import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300
JUGADOR_1 = "x"
JUGADOR_2 = "o"

def alternar_jugador(turno):
    """Determinar de quién es el turno"""
    """alternar entre los dos jugadores"""
    if turno == JUGADOR_1:
        turno = JUGADOR_2
    else:
        turno = JUGADOR_1
def juego_crear():
    """Crear el tablero"""
    """el tablero es un diccionario que tiene como claves las posiciones del tablero y como valor el símbolo del jugador que
    hizo la jugada en esa posición. Por ejemplo, si el jugador 1 hizo una jugada en la posición (0, 0), entonces el diccionario
    tendrá la clave (0, 0) con el valor "x". Si el jugador 2 hizo una jugada en la posición (1, 2), entonces el diccionario tendrá
    la clave (1, 2) con el valor "o"."""
    juego = {}
    for i in range(10):
        for j in range(10):
            juego[i, j] = 0
    return juego

def alternar_jugador(turno):
    """Determinar de quién es el turno"""
    """alternar entre los dos jugadores"""
    if turno == JUGADOR_1:
        turno = JUGADOR_2
    else:
        turno = JUGADOR_1
def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    """En la función juego_actualizar tenemos que actualizar el tablero con la jugada del usuario.
    Para eso, primero tenemos que averiguar en qué celda del tablero se hizo click.
    Para eso, tenemos que dividir la posición del click por el tamaño de cada celda.
    """
    x = x // 30
    y = y // 30
    """juego es un diccionario que tiene como claves las posiciones del tablero y como valor el símbolo del jugador que hizo la jugada en esa posición."""
    """Tamibién tenemos que determinar de quién es el turno y actualizar el tablero con la jugada del usuario."""
    turno = JUGADOR_1
    if juego[x][y] == 0:
        juego[x][y] = turno
        turno = alternar_jugador(turno)
    return juego


def juego_mostrar(juego):
    """Actualizar la ventana"""
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero y mostrar de 
    quién es el turno. ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con utilizar las funciones 
    draw_text y draw_rectangle/draw_line"""
    """Dibujar el tablero"""

    gamelib.draw_rectangle(0, 0, 300, 300, fill='yellow')
    for i in range(10):
        for j in range(10):
            gamelib.draw_line(i * 30, 0, i * 30, 300, fill='blue', width=2)
            gamelib.draw_line(0, j * 30, 300, j * 30, fill='blue', width=2)
            """Acceder a las claves del diccionario juego que son las posiciones del tablero"""












def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)