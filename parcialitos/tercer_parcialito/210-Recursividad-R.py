"""Dada una Cola cuyas únicas primitivas son encolar y desencolar, escribir una función recursiva que invierta
in-place los elementos de la misma. No se permite usar estructuras auxiliares."""
from cola import Cola
from pila import Pila

def invertir_cola(cola):
    """Invierte el orden de los elementos de una cola, usando nodos auxiliares"""
    if cola.esta_vacia():
        return
    else:
        dato = cola.desencolar()
        invertir_cola(cola)
        cola.encolar(dato)

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
print(cola)
invertir_cola(cola)
print(cola)