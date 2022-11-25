"""Dada una pila y un número n que representa una cantidad de elementos, se pide implementar una función que devuelva
una lista con pilas de n elementos, preservando el orden de los elementos en la pila original. La pila original debe
quedar vacía. Ejemplo:
dividir_pila(Pila(1,2,3,4,8,6,7), 3)
   → [Pila(1,2,3), Pila(4,8,6), Pila(7)]
Nota: el tope de las pilas representadas es el primer elemento listado; por ejemplo, el tope de la pila original es el 1."""
from pila import Pila

def dividir_pila(pila, n):
    """Devuelve una lista con pilas de n elementos, preservando el orden de los elementos en la pila original.
    La pila original debe quedar vacía."""
    lista = []
    while not pila.esta_vacia():
        pila_aux = Pila()
        for i in range(n):
            if not pila.esta_vacia():
                pila_aux.apilar(pila.desapilar())
        lista.append(pila_aux)
    return lista

p = Pila()
p.apilar(2)
p.apilar(3)
p.apilar(1)
p.apilar(4)
p.apilar(5)
p.apilar(6)
p.apilar(7)
p.apilar(8)
p.apilar(9)

print(dividir_pila(p, 3))
