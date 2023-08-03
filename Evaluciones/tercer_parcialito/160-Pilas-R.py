"""Escribir una función que reciba por parámetro dos pilas y modifique su contenido de manera que los elementos
de la primer pila queden en la segunda, y los de la segunda en la primera manteniendo el orden original de los
elementos. Como estructuras auxiliares, se pueden utilizar únicamente pilas y/o colas."""

from pila import Pila
from cola import Cola

def invertir_pilas(pila1, pila2):
    """Escribir una funcion que reciba por parametro dos pilas y modifique su contenido de manera que los elementos
    de la primera pila queden en la segunda, y los de la segunda en la primera manteniendo el orden original de los
    elementos. Como estructuras auxiliares, se pueden utilizar unicamente pilas y/o colas.
    """
    pila_aux1 = Pila()
    pila_aux2 = Pila()
    while not pila1.esta_vacia():
        pila_aux1.apilar(pila1.desapilar())
    while not pila2.esta_vacia():
        pila_aux2.apilar(pila2.desapilar())
    while not pila_aux1.esta_vacia():
        pila2.apilar(pila_aux1.desapilar())
    while not pila_aux2.esta_vacia():
        pila1.apilar(pila_aux2.desapilar())



pila1 = Pila()
pila1.apilar(5)
pila1.apilar(4)
pila1.apilar(3)
pila1.apilar(2)
pila1.apilar(1)

pila2 = Pila()
pila2.apilar(11)
pila2.apilar(10)
pila2.apilar(9)
pila2.apilar(8)
pila2.apilar(7)
pila2.apilar(6)


print(pila1)
print(pila2)
invertir_pilas(pila1, pila2)
print(pila1)
print(pila2)