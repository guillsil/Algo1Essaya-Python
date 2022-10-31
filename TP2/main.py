import soko
import gamelib
import soko

ANCHO_VENTANA = 300
ALTO_VENTANA = 300




def main():
    # Inicializar el estado del juego
    nivel = 0
    grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))

    max_col = soko.hallar_max_columnas(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))

    ancho_ventana = max_col * 60
    alto_ventana = grilla[4][1] * 60
    gamelib.resize(ancho_ventana, alto_ventana)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        soko.juego_mostrar(grilla)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        if tecla == "W" or tecla == "w":
            movimiento = NORTE
            grilla = mover(grilla, movimiento)
        elif tecla == "S" or tecla == "s":
            movimiento = SUR
            grilla = mover(grilla, movimiento)
        elif tecla == "A" or tecla == "a":
            movimiento = OESTE
            grilla = mover(grilla, movimiento)
        elif tecla == "D" or tecla == "d":
            movimiento = ESTE
            grilla = mover(grilla, movimiento)
        elif tecla == "Q" or tecla == "q":
            #tecla para reiniciar nivel
            grilla = reiniciar_nivel(nivel)
        else:
            print("Direccion invalida, intente nuevamente")
            continue
        # Verificar si el jugador ganó o perdió
        if soko.juego_ganado(grilla):
            print("Ganaste!")
            nivel += 1
            grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))
            max_col = soko.hallar_max_columnas(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))
            ancho_ventana = max_col * 60
            alto_ventana = grilla[4][1] * 60
            gamelib.resize(ancho_ventana, alto_ventana)
        #gano el juego completo
        if nivel > 153:
            print("Ganaste el juego completo!")
            break
gamelib.init(main)