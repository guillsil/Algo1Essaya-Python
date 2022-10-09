def juego_mostrar(juego):
    """Actualizar la ventana"""
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero y mostrar de 
    quién es el turno. ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con utilizar las funciones 
    draw_text y draw_rectangle/draw_line"""
    """Dibujar el tablero"""
    turno = JUGADOR_1
    gamelib.draw_rectangle(0, 0, 300, 390, fill='#080F28')
    gamelib.draw_rectangle(0, 60, 300, 360, fill='#dda90e')
    """Mostrar de quién es el turno"""
    gamelib.draw_text("Turno de: " + turno, 150, 30, fill='#dda90e', size=20)
    for i in range(10):
        for j in range(13):
            gamelib.draw_line(i * 30, 60, i * 30, 360, fill='#080F28', width=2)
            gamelib.draw_line(0, j * 30, 330, j * 30, fill='#080F28', width=2)
    """Dibujar las fichas"""
    for i in range(10):
        for j in range(10):
            if juego[i, j] == JUGADOR_1:
                gamelib.draw_text(JUGADOR_1, i * 30 + 15, j * 5 + 75, fill='#080F28')
            elif juego[i, j] == JUGADOR_2:
                gamelib.draw_text(JUGADOR_2, i * 30 + 15, j * 30 + 75, fill='#080F28')
    "mostrar el nombre de los jugadores"
    gamelib.draw_text("Jugador 1: " + JUGADOR_1, 60, 375, fill='#dda90e', size=10)
    gamelib.draw_text("Jugador 2: " + JUGADOR_2, 240, 375, fill='#dda90e', size=10)





def juego_mostrar(juego):
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
                gamelib.draw_text(JUGADOR_1, i * 30 + 15, j * 30 + 15, fill='#080F28')
            elif juego[i, j] == JUGADOR_2:
                gamelib.draw_text(JUGADOR_2, i * 30 + 15, j * 30 + 15, fill='#080F28')

    """Mostrar de quién es el turno"""
    gamelib.draw_text("Turno de: " , 150, 330, fill='#dda90e', size=20)
    "mostrar el nombre de los jugadores"
    gamelib.draw_text("Jugador 1: " + JUGADOR_1, 60, 375, fill='#dda90e', size=12)
    gamelib.draw_text("Jugador 2: " + JUGADOR_2, 240, 375, fill='#dda90e', size=12)

