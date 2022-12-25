def actualizar_estado(grilla, tecla, nivel):
    """Actualiza el estado del juego, según la `tecla` presionada.
    Devuelve el nuevo estado del juego.
    """
    teclas = cargar_teclas("teclas.txt")
    for accion in teclas:
        if accion == "NORTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, NORTE)
        elif accion == "SUR":
            if tecla in teclas[accion]:
                grilla = mover(grilla, SUR)
        elif accion == "ESTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, ESTE)
        elif accion == "OESTE":
            if tecla in teclas[accion]:
                grilla = mover(grilla, OESTE)
        elif accion == "REINICIAR":
            if tecla in teclas[accion]:
                grilla = reiniciar_nivel(nivel)
        elif accion == "NEXT_LEVEL":
            if tecla in teclas[accion]:
                nivel += 1
                if nivel > 153:
                    raise ValueError("No hay mas niveles")
                grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", nivel))[0])
                ancho_ventana, alto_ventana = refrescar_ventana(grilla)
                gamelib.resize(ancho_ventana, alto_ventana)
        elif accion == "PREV_LEVEL":
            if tecla in teclas[accion]:
                nivel -= 1
                if nivel < 0:
                    raise ValueError("No hay niveles anteriores")
                grilla = crear_grilla(completar_grilla(leer_nivel("niveles.txt", nivel))[0])
                ancho_ventana, alto_ventana = refrescar_ventana(grilla)
                gamelib.resize(ancho_ventana, alto_ventana)
    return grilla, nivel


import gamelib
from pila import Pila
import soko

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

"""Deshacer y rehacer
En el caso de que el usuario se equivoque o decida probar una combinación diferente de movimientos, el juego
debería permitir deshacer y rehacer los diferentes movimientos.
El "deshacer" permite revertir los últimos movimientos. Para esto el juego debe tener la capacidad de
recordar una cantidad ilimitada de grillas previas, y si deshacemos repetidas veces deberíamos siempre
poder llegar al estado inicial del nivel.
Por otro lado, el "rehacer" permite "deshacer el deshacer" y solo tiene efecto luego de haber hecho "deshacer"
una o más veces seguidas. La idea es que el usuario tenga la opción de usar "deshacer" y "rehacer" todas las
veces que quiera para visualizar el cambio de la grilla en sentido inverso (al "deshacer") y en sentido directo 
(al "rehacer"). En cualquier momento en el que el usuario hace cualquier acción que no sea "deshacer" o "rehacer"
, pierde la posibilidad de "rehacer" hasta la próxima vez que haga "deshacer".
Estas funcionalidades se implementan con un par de pilas.
Se deberá deshacer y rehacer presionando teclas correspondientes para cada acción (configurable mediante teclas.txt).
"""


class Mover:
    def __init__(self, grilla, tecla, nivel):
        self.grilla = grilla
        self.tecla = tecla
        self.nivel = nivel
        self.pila_deshacer = Pila()
        self.pila_rehacer = Pila()

    def mover(self):
        # guardar el estado actual
        self.pila_deshacer.apilar(self.grilla)
        teclas = soko.cargar_teclas("teclas.txt")
        # si se presiona una tecla
        for accion in teclas:
            if accion == "NORTE":
                if self.tecla in teclas[accion]:
                    self.grilla = soko.mover(self.grilla, NORTE)
                    self.pila_deshacer.apilar(self.grilla)
            elif accion == "SUR":
                if self.tecla in teclas[accion]:
                    self.grilla = soko.mover(self.grilla, SUR)
                    self.pila_deshacer.apilar(self.grilla)
            elif accion == "ESTE":
                if self.tecla in teclas[accion]:
                    self.grilla = soko.mover(self.grilla, ESTE)
                    self.pila_deshacer.apilar(self.grilla)
            elif accion == "OESTE":
                if self.tecla in teclas[accion]:
                    self.grilla = soko.mover(self.grilla, OESTE)
                    self.pila_deshacer.apilar(self.grilla)
            elif accion == "REINICIAR":
                if self.tecla in teclas[accion]:
                    self.grilla = self.reiniciar()
            elif accion == "NEXT_LEVEL":
                if self.tecla in teclas[accion]:
                    self.nivel += 1
                    if self.nivel > 153:
                        raise ValueError("No hay mas niveles")
                    self.grilla = soko.crear_grilla(
                        soko.completar_grilla(soko.leer_nivel("niveles.txt", self.nivel))[0])
                    ancho_ventana, alto_ventana = soko.refrescar_ventana(self.grilla)
                    gamelib.resize(ancho_ventana, alto_ventana)
            elif accion == "PREV_LEVEL":
                if self.tecla in teclas[accion]:
                    self.nivel -= 1
                    if self.nivel < 0:
                        raise ValueError("No hay niveles anteriores")
                    self.grilla = soko.crear_grilla(
                        soko.completar_grilla(soko.leer_nivel("niveles.txt", self.nivel))[0])
                    ancho_ventana, alto_ventana = soko.refrescar_ventana(self.grilla)
                    gamelib.resize(ancho_ventana, alto_ventana)

            elif accion == "DESHACER":
                if self.tecla in teclas[accion]:
                    if not self.pila_deshacer.esta_vacia():
                        self.pila_rehacer.apilar(self.pila_deshacer.desapilar())
                        self.grilla = self.pila_deshacer.ver_tope()
            elif accion == "REHACER":
                if self.tecla in teclas[accion]:
                    if not self.pila_rehacer.esta_vacia():
                        self.pila_deshacer.apilar(self.pila_rehacer.desapilar())
                        self.grilla = self.pila_deshacer.ver_tope()

        return self.grilla, self.nivel














