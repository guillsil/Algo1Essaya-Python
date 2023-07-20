"""Escribir un método de la clase ListaEnlazada que invierta el orden de la lista
(es decir, el primer elemento queda como último y viceversa)."""
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

    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.siguiente
        return f"Lista Enlazada({', '.join(lista)})"
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
    def invertir_lista(self):
        actual = self.primero
        anterior = None
        while actual != None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.primero = anterior

mi_lista = ListaEnlazada()

mi_nodo1 = Nodo(1)
mi_nodo2 = Nodo(5)
mi_nodo3 = Nodo(8)
mi_nodo4 = Nodo(8)
mi_nodo5 = Nodo(2)

mi_lista.primero = mi_nodo1
mi_nodo1.siguiente = mi_nodo2
mi_nodo2.siguiente = mi_nodo3
mi_nodo3.siguiente = mi_nodo4
mi_nodo4.siguiente = mi_nodo5
print(mi_lista)
mi_lista.invertir_lista()
print(mi_lista)








