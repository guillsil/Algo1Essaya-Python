import gamelib

ANCHO_VENTANA = 300
ALTO_VENTANA = 300

def juego_crear():
    """Inicializar el estado del juego"""
    """Crear el tablero"""
    tablero = []
    for i in range(10):
        tablero.append([0] * 10)
    return tablero

def mostrar_tablero(tablero):
    """Mostrar el tablero"""
    for fila in tablero:
        print(fila)


def estaOcupado(tablero, x, y):
    """Verificar si la posicion esta ocupada"""
    if tablero[x][y] == 0:
        return False
    else:
        return True

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego
    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    """Actualizar el tablero"""
    """En la función juego_actualizar tenemos que actualizar el tablero con la jugada del usuario.
    Para eso, primero tenemos que averiguar en qué celda del tablero se hizo click.
    Para eso, tenemos que dividir la posición del click por el tamaño de cada celda.
    Por ejemplo, si el usuario hizo click en la posición (50, 50), y cada celda mide 10x10,
    entonces la celda en la que hizo click es la de la fila 5 y la columna 5.
    """
    """donde se hizo click"""
    x = x // 30
    y = y // 30
    """verificar si la posicion esta ocupada"""
    if estaOcupado(juego, x, y):
        print("La posicion esta ocupada")
    else:
        juego[x][y] = "x"
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
            gamelib.draw_line(i * 30, 0, i * 30, 300, fill='blue', width=2, dash=(4, 4))
            gamelib.draw_line(0, j * 30, 300, j * 30, fill='blue', width=2, dash=(4, 4))
            if juego[i][j] == "x":
                gamelib.draw_text(i * 30 + 15, j * 30 + 15, "x", fill='red', font=("Arial", 30))
            elif juego[i][j] == "o":
                gamelib.draw_text(i * 30 + 15, j * 30 + 15, "o", fill='blue', font=("Arial", 30))
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
