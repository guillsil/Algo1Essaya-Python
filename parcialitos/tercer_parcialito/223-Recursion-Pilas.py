"""Escribir una función recursiva que reciba una pila la modifique de tal forma que el valor del tope se mueva hacia el fondo, manteniendo el orden del resto de los elementos.

Por ejemplo, para la siguiente pila:

fondo >| 5, 4, 3, 2, 1 >| tope

La función debe modificarla para que quede:

fondo >| 1, 5, 4, 3, 2 >| tope

"""
from pila import Pila

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
pila.apilar(5)


#ITERATIVA
def mover_tope(pila):
    aux = Pila()
    while not pila.esta_vacia():
        aux.apilar(pila.desapilar())
    tope = aux.desapilar()
    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())
    pila.apilar(tope)
print(pila)
mover_tope(pila)
print(pila)