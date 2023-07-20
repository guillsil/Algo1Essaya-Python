"""Implementar una función que, dada una pila de números, devuelva otra pila que contenga únicamente los números
pares de ésta (manteniendo el orden relativo de los elementos según como estaban en la original). La pila original
debe preservar su estado original al salir de la función. Es decir, debe conservar todos los elementos que tenía y
el orden de los mismos antes de que la función fuese invocada."""
from pila import Pila
def pares(pila):
    pila_aux = Pila()
    pila_resultado = Pila()
    while not pila.esta_vacia():
        dato = pila.desapilar()
        pila_aux.apilar(dato)
        if dato % 2 == 0:
            pila_resultado.apilar(dato)
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    return pila_resultado