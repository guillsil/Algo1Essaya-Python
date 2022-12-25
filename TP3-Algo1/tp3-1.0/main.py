import gamelib
import soko
from mover import Movimiento

def main():
    # Inicialqizar el estado del juego
    nivel = 0
    name_level = ""
    desc = soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel))[0]
    grilla = soko.crear_grilla(desc)

    ancho_ventana, alto_ventana = soko.refrescar_ventana(grilla)
    gamelib.resize(ancho_ventana, alto_ventana)

    while gamelib.is_alive():
        gamelib.draw_begin()
        # Dibujar la pantalla
        soko.juego_mostrar(grilla)
        # cambiar texto de la ventana
        name_level = soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel))[1]
        gamelib.title("Sokoban # - Nivel {} - {}".format(nivel + 1, name_level))
        gamelib.draw_end()

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        movimiento = Movimiento(grilla, tecla, nivel)
        grilla, nivel = movimiento.mover()


        # Verificar si el jugador ganó o perdió
        if soko.juego_ganado(grilla):
            print("Ganaste!")
            nivel += 1
            grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel))[0])
            ancho_ventana, alto_ventana = soko.refrescar_ventana(grilla)
            gamelib.resize(ancho_ventana, alto_ventana)
            name_level = soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel))[1]

        #gano el juego completo y se cierra la ventana, lanzar un exception de juego finalizado
        if nivel > 153:
            raise Exception("Juego finalizado")

gamelib.init(main)