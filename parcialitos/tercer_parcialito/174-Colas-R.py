"""Escribir una función que recibe una cola e invierte el orden de sus elementos. La función debe modificar
la Cola recibida, no devolver una nueva ni tampoco debe usar estructuras auxiliares."""
from cola import Cola
from pila import Pila

def invertir_cola(cola):
    """Invierte el orden de los elementos de una cola, usando nodos auxiliares"""
    pila = Pila()
    while not cola.esta_vacia():
        pila.apilar(cola.desencolar())
    while not pila.esta_vacia():
        cola.encolar(pila.desapilar())

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
print(cola)
invertir_cola(cola)
print(cola)