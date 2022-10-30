"""Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
elemento y duplica todas las apariciones del mismo. Ejemplo:
L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
L.duplicar(8) => L = 1 -> 5 -> 8 -> 8 -> 8 -> 8 -> 2 -> 8 -> """
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.prox = None
        self.len = 0
    def duplicar(self, elemento):
        actual = self.primero
        anterior = None
        while actual != None:
            if actual.dato == elemento:
                nuevo = Nodo(elemento)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                anterior = actual
                actual = actual.siguiente
            anterior = actual
            actual = actual.siguiente
