"""Escribir una función que calcule recursivamente cuántos elementos hay en una
pila, suponiendo que la pila sólo tiene los métodos apilar y desapilar, y no altere el contenido
de la pila."""
from pila import Pila
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)
def cantidad_elementos(pila):
    if pila.esta_vacia():
        return 0
    else:
        pila.desapilar()
        return 1 + cantidad_elementos(pila)
print(cantidad_elementos(pila))