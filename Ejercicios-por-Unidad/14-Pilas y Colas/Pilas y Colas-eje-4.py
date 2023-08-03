"""Juego de Cartas
a) Crear una clase Carta que contenga un palo y un valor.
b) Crear una clase Solitario que permita apilar las cartas una arriba de otra, pero sólo
permita apilar una carta si es de un número inmediatamente inferior y de distinto palo
a la carta que está en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una
excepción."""
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

class Solitario:
    def __init__(self):
        self.tope = None
    def apilar(self, carta):
        if self.tope is None:
            self.tope = carta
        else:
            if carta.valor == self.tope.valor - 1 and carta.palo != self.tope.palo:
                self.tope = carta
            else:
                raise ValueError("No se puede apilar la carta")
#probar
s = Solitario()
s.apilar(Carta("Oro", 12))
s.apilar(Carta("Basto", 11))
s.apilar(Carta("Copa", 10))
s.apilar(Carta("Espada", 9))
s.apilar(Carta("Espada", 8))
