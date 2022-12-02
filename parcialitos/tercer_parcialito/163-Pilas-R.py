"""Implementar una función que calcule el promedio de los elementos de una pila de números que recibe por parámetro.
La pila debe quedar en el mismo estado en el que fue recibida (con los mismos elementos y en el mismo orden)."""
from pila import Pila
def promedio(pila):
    pila_aux = Pila()
    suma = 0
    cantidad = 0
    while not pila.esta_vacia():
        dato = pila.desapilar()
        suma += dato
        cantidad += 1
        pila_aux.apilar(dato)
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    return suma / cantidad