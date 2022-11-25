"""Crear una clase Carta que contenga un palo y un valor, y una clase Solitario que permita apilar las cartas
una arriba de otra.
Solo permite apilar una carta si es de un número inmediatamente inferior y de distinto palo a la carta que está
en el tope. Si se intenta apilar una carta incorrecta, debe lanzar una excepción.
Ejemplo
>> solitario = Solitario()
>> solitario.apilar(Carta('Copa', 12))
>> solitario.apilar(Carta('Oro', 11))
>> solitario.apilar(Carta('Oro', 10))
Exception: Carta inválida
>> solitario.apilar(Carta('Espada', 11))
Exception: Carta inválida
>> solitario.apilar(Carta('Copa', 9))
Exception: Carta inválida
>> solitario.apilar(Carta('Copa', 10))
>>
Nota: Se encuentran disponibles los TDA Pila y Cola con sus métodos ya definidos en los archivos pila.py
y cola.py respectivamente."""
from pila import Pila
from cola import Cola
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

