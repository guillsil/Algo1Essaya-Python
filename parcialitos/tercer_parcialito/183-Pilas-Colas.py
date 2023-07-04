"""Escribir una función clonar_pila, que reciba por parámetro una pila y devuelva una nueva pila con los elementos de la primera manteniendo el orden original.

Nota: la pila recibida debe quedar en su estado original.
"""

from cola import Cola
from pila import Pila

def clonar_pila(pila):
    pila_aux = Pila()
    pila_clonada = Pila()
    while not pila.esta_vacia():
        pila_aux.apilar(pila.desapilar())
    while not pila_aux.esta_vacia():
        dato = pila_aux.desapilar()
        pila_clonada.apilar(dato)
        pila.apilar(dato)
    return pila_clonada


pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)
print(pila)
pila_clonada = clonar_pila(pila)
print(pila_clonada)
