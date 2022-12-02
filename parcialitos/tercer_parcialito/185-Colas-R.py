"""Implementar una función que calcule el promedio de los elementos de una cola de números que recibe por parámetro.
La cola debe quedar en el mismo estado en el que fue recibida (con los mismos elementos y en el mismo orden)"""
from cola import Cola
def promedio(cola):
    cola_aux = Cola()
    suma = 0
    cantidad = 0
    while not cola.esta_vacia():
        dato = cola.desencolar()
        suma += dato
        cantidad += 1
        cola_aux.encolar(dato)
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    return suma / cantidad
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)

print(promedio(cola))