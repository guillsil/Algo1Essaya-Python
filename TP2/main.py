import soko
import gamelib
import soko

ANCHO_VENTANA = 300
ALTO_VENTANA = 300




def main():
    # Inicializar el estado del juego
    nivel = 0
    grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))

    ancho_ventana, alto_ventana = soko.refrescar_ventana(grilla, nivel)
    gamelib.resize(ancho_ventana, alto_ventana)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        soko.juego_mostrar(grilla)
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        grilla, nivel = soko.actualizar_estado(grilla, tecla, nivel)
        # Verificar si el jugador ganó o perdió
        if soko.juego_ganado(grilla):
            print("Ganaste!")
            nivel += 1
            grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))
            ancho_ventana, alto_ventana = soko.refrescar_ventana(grilla, nivel)
            gamelib.resize(ancho_ventana, alto_ventana)
        #gano el juego completo
        if nivel > 153:
            print("Ganaste el juego completo!")
            break
gamelib.init(main)