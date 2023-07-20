import gamelib
from pila import Pila
import soko

OESTE = (-1, 0)
ESTE = (1, 0)
NORTE = (0, -1)
SUR = (0, 1)

class Movimiento:
    def __init__(self, grilla, tecla, nivel):
        self.grilla = grilla
        self.tecla = tecla
        self.nivel = nivel
        self.moves_made = Pila()
        self.moves_aux = Pila()
    def mover(self):
        teclas = soko.cargar_teclas("teclas.txt")
        self.moves_made.apilar(self.grilla)
        for accion in teclas:
            if accion == "NORTE":
                if self.tecla in teclas[accion]:
                    self.moves_made.apilar(self.grilla)
                    self.grilla = soko.mover(self.grilla, NORTE)
                    #si se mueve, se guarda el movimiento en la pila de movimientos realizados
                    self.moves_made.apilar(self.grilla)
            elif accion == "SUR":
                if self.tecla in teclas[accion]:
                    self.moves_made.apilar(self.grilla)
                    self.grilla = soko.mover(self.grilla, SUR)
                    self.moves_made.apilar(self.grilla)
            elif accion == "ESTE":
                if self.tecla in teclas[accion]:
                    self.moves_made.apilar(self.grilla)
                    self.grilla = soko.mover(self.grilla, ESTE)
                    self.moves_made.apilar(self.grilla)
            elif accion == "OESTE":
                if self.tecla in teclas[accion]:
                    self.moves_made.apilar(self.grilla)
                    self.grilla = soko.mover(self.grilla, OESTE)
                    self.moves_made.apilar(self.grilla)
            #Inplemetar deshacer y rehacer
            elif accion == "DESHACER":
                if self.tecla in teclas[accion]:
                    self.moves_aux.apilar(self.moves_made.desapilar())
                    self.moves_made.desapilar()
                    self.grilla = self.moves_made.ver_tope()
                    #si se deshace, se guarda el movimiento en la pila de movimientos auxiliares
            elif accion == "REHACER":
                if self.tecla in teclas[accion]:
                    self.moves_made.apilar(self.moves_aux.desapilar())
                    self.grilla = self.moves_made.ver_tope()
                    #si se rehace, se guarda el movimiento en la pila de movimientos realizados
        return self.grilla, self.nivel
    
