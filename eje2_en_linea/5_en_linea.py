import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 390
ANCHO_PIXELS = 30
ALTO_PIXELS = 30
MAX_ALTO = 10
MAX_ANCHO = 10

JUGADOR_1 = "X"
JUGADOR_2 = "O"

def juego_crear():
    #Crear el tablero
    """El tablero es un diccionario que tiene como claves las posiciones del tablero y como valor el símbolo del jugador que
    hizo la jugada en esa posición."""
    juego = {}
    for i in range(MAX_ANCHO):
        for j in range(MAX_ALTO):
            juego[i, j] = 0
    return juego, JUGADOR_1
def juego_actualizar(juegos, x, y):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    juego, turno = juegos
    x = x // ANCHO_PIXELS
    y = y // ALTO_PIXELS
    #asegurarse de que NO se pueda pasar el tablero y que no se pueda pisar una ficha
    if x < MAX_ANCHO and y < MAX_ALTO and  juego[x, y] == 0:
        if turno == JUGADOR_1:
            juego[x, y] = JUGADOR_1
            turno = JUGADOR_2
        else:
            juego[x, y] = JUGADOR_2
            turno = JUGADOR_1
    return juego, turno

def juego_mostrar(juegos):
    #Actualizar la ventana
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero y mostrar de 
    quién es el turno. ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con utilizar las funciones 
    draw_text y draw_rectangle/draw_line"""
    """Dibujar el tablero"""
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA, fill='#080F28')
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ANCHO_VENTANA, fill='#dda90e')
    juego, turno = juegos
    for i in range(MAX_ANCHO):
        for j in range(MAX_ALTO):
            gamelib.draw_line(i * 30, 0, i * 30, 360, fill='#080F28', width=2)
            gamelib.draw_line(0, j * 30, 330, j * 30, fill='#080F28', width=2)
    #Dibujar las fichas
    for i in range(MAX_ANCHO):
        for j in range(MAX_ALTO):
            if juego[i, j] == JUGADOR_1:
                gamelib.draw_text(JUGADOR_1, i * 30 + 15, j * 30 + 15, fill='#080F28',size=15)
            elif juego[i, j] == JUGADOR_2:
                gamelib.draw_text(JUGADOR_2, i * 30 + 15, j * 30 + 15, fill='#080F28',size=15)

    #Mostrar de quién es el turno
    gamelib.draw_text("Turno de: " + turno, 150, 330, fill='#dda90e', size=20)
    #mostrar el nombre de los jugadores
    gamelib.draw_text("Jugador 1: " + JUGADOR_1, 60, 375, fill='#dda90e', size=12)
    gamelib.draw_text("Jugador 2: " + JUGADOR_2, 240, 375, fill='#dda90e', size=12)

def main():
    juegos = juego_crear()
    juego, turno = juegos
    # Ajustar el tamaño de la ventana
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juegos)
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
            juegos = juego_actualizar(juegos, x, y)
gamelib.init(main)