import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 390
JUGADOR_1 = "X"
JUGADOR_2 = "O"
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
        return JUGADOR_2
    else:
        return JUGADOR_1

def juego_actualizar(juego, x, y, turno):
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
    """juego es un diccionario que tiene como claves las posiciones del tablero y como valor el símbolo del jugador que hizo la jugada en esa posición.
    Tambien debo cambiar el turno del jugador
    """
    juego[x, y] = turno

    return juego

def esta_ocupado(juego, x, y):
    """Determinar si una celda está ocupada"""
    """En la función esta_ocupado tenemos que determinar si una celda está ocupada.
    es decir no contiene a uno de los jugadores
    """
    return juego[x, y] != 0

def juego_mostrar(juego, turno):
    """Actualizar la ventana"""
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero y mostrar de 
    quién es el turno. ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con utilizar las funciones 
    draw_text y draw_rectangle/draw_line"""
    """Dibujar el tablero"""
    gamelib.draw_rectangle(0, 0, 300, 390, fill='#080F28')
    gamelib.draw_rectangle(0, 0, 300, 300, fill='#dda90e')

    for i in range(10):
        for j in range(10):
            gamelib.draw_line(i * 30, 0, i * 30, 360, fill='#080F28', width=2)
            gamelib.draw_line(0, j * 30, 330, j * 30, fill='#080F28', width=2)
    """Dibujar las fichas"""
    for i in range(10):
        for j in range(10):
            if juego[i, j] == JUGADOR_1:
                gamelib.draw_text(JUGADOR_1, i * 30 + 15, j * 30 + 15, fill='#080F28',size=15)
            elif juego[i, j] == JUGADOR_2:
                gamelib.draw_text(JUGADOR_2, i * 30 + 15, j * 30 + 15, fill='#080F28',size=15)

    """Mostrar de quién es el turno"""
    gamelib.draw_text("Turno de: " + turno , 150, 330, fill='#dda90e', size=20)
    "mostrar el nombre de los jugadores"
    gamelib.draw_text("Jugador 1: " + JUGADOR_1, 60, 375, fill='#dda90e', size=12)
    gamelib.draw_text("Jugador 2: " + JUGADOR_2, 240, 375, fill='#dda90e', size=12)


def main():
    juego = juego_crear()
    turno = JUGADOR_2
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego, turno)
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
            if not esta_ocupado(juego, x // 30, y // 30):
                juego = juego_actualizar(juego, x, y, turno)
                turno = alternar_jugador(turno)


gamelib.init(main)