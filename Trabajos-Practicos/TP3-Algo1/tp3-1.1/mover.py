from pila import Pila
from cola import Cola
from soko import *
import main

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

class JuegoMover:
    """Apuntes -Clase para controlar las acciones del juego"""
    def __init__(self, grilla, tecla, nivel):
        self.grilla = grilla
        self.tecla = tecla
        self.nivel = nivel
        self.hacer = Pila()
        self.rehacer_deshacer = Pila()
        self.solucion = Cola()
        self.teclas = main.cargar_teclas()
        self.niveles = main.lista_niveles()

    def actualizar_estado(self):
        tamanio = dimencion_grilla(self.grilla)
        # si la tecla no esta en el diccionario de teclas, no hacer nada
        if self.tecla not in self.teclas:
            return self.grilla, self.nivel
        # si la tecla esta en el diccionario de teclas, ejecutar la accion correspondiente
        if self.teclas[self.tecla] == "OESTE":
            grilla = mover(self.grilla, OESTE)
            # cargar en la pila la grilla con el movimiento
            self.hacer.apilar(grilla.copy())
        elif self.teclas[self.tecla] == "ESTE":
            grilla = mover(self.grilla, ESTE)
            # cargar en la pila la grilla con el movimiento
            self.hacer.apilar(grilla.copy())
        elif self.teclas[self.tecla] == "NORTE":
            grilla = mover(self.grilla, NORTE)
            # cargar en la pila la grilla con el movimiento
            self.hacer.apilar(grilla.copy())
        elif self.teclas[self.tecla] == "SUR":
            grilla = mover(self.grilla, SUR)
            # cargar en la pila la grilla con el movimiento
            self.hacer.apilar(grilla.copy())
        elif self.teclas[self.tecla] == "DESHACER":
            if not self.hacer.esta_vacia():
                # cargar en la pila la grilla con el movimiento
                self.rehacer_deshacer.apilar(self.grilla.copy())
                grilla = self.hacer.ver_tope()
                self.hacer.desapilar()
        elif self.teclas[self.tecla] == "REHACER":
            if not self.rehacer_deshacer.esta_vacia():
                # cargar en la pila la grilla con el movimiento
                self.hacer.apilar(self.grilla.copy())
                grilla = self.rehacer_deshacer.ver_tope()
                self.rehacer_deshacer.desapilar()
        return self.grilla, self.nivel
    
