"""Escribir una función recursiva que reciba una pila la modifique de tal forma que el valor del tope se mueva
hacia el fondo, manteniendo el orden del resto de los elementos.
Por ejemplo, para la siguiente pila:

fondo >| 5, 4, 3, 2, 1 >| tope

La función debe modificarla para que quede:

fondo >| 1, 5, 4, 3, 2 >| tope

"""
from pila import Pila
from cola import Cola

def mover_tope(pila):
    """Escribir una funcion recursiva que reciba una pila la modifique de tal forma que el valor del tope se mueva
    hacia el fondo, manteniendo el orden del resto de los elementos.
    """
    cola = Cola()
    if pila.esta_vacia():
        return
    else:
        dato = pila.desapilar()
        mover_tope(pila)
        while not pila.esta_vacia():
            cola.encolar(pila.desapilar())
        pila.apilar(dato)
        while not cola.esta_vacia():
            pila.apilar(cola.desencolar())

    




pila = Pila()
pila.apilar(5)
pila.apilar(4)
pila.apilar(3)
pila.apilar(2)
pila.apilar(1)
print(pila)
print(pila.ver_tope())
mover_tope(pila)
print(pila)
print(pila.ver_tope())

