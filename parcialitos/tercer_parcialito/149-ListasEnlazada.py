"""Implementar un método de la clase ListaEnlazada que elimine sobre la misma lista los elementos consecutivos repetidos. La misma está implementada con únicamente una referencia al primer nodo.

L: [3 4 4 4 1 4] → L.eliminar_consecutivos() → L: [3 4 1 4]

"""
import listaEnlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar_elemento(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo

    def eliminar_consecutivos(self):
        if self.primero is None:
            return

        actual = self.primero
        while actual.siguiente is not None:
            if actual.dato == actual.siguiente.dato:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

    def __str__(self):
        if self.primero is None:
            return "[]"

        actual = self.primero
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " ".join(elementos) + "]"
    def sumaAcumulativa9

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(3)
lista.agregar_elemento(4)

print(lista)
lista.eliminar_consecutivos()
print(lista)