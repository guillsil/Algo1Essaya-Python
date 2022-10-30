"""Implementar el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve
 de la lista todas las apariciones del mismo, devolviendo la cantidad
de elementos removidos. La lista debe ser recorrida una sola vez."""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.prox = None
        self.len = 0
    def remover_todos(self, elemento):
        actual = self.primero
        anterior = None
        cantidad = 0
        while actual != None:
            if actual.dato == elemento:
                if anterior == None:
                    self.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                cantidad += 1
            anterior = actual
            actual = actual.siguiente
        return cantidad





