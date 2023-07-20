"""Dada una clase ListaEnlazada con referencia al primer nodo, escribir un método que modifique la lista para que
invierta el orden de cada k elementos por grupo, donde k > 0.

Por ejemplo, para la lista:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
Con k = 3, debe modificarse para que quede:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7
Con k = 4, debe modificarse para que quede:
4 -> 3 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
Se permite el uso de Pilas y Colas como estructuras auxiliares."""
from pila import Pila
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.prox
        return f"Lista Enlazada({', '.join(lista)})"
    def invertir(self, k):
        """Invierte el orden de cada k elementos por grupo"""
        if k <= 0:
            return
        if self.primero is None:
            return
        actual = self.primero
        pila = Pila()
        while actual is not None:
            for i in range(k):
                if actual is None:
                    break
                pila.apilar(actual.dato)
                actual = actual.prox
            for i in range(k):
                if pila.esta_vacia():
                    break
                self.primero.dato = pila.desapilar()
                self.primero = self.primero.prox




li = ListaEnlazada()
li.primero = _Nodo("1")
li.primero.prox = _Nodo("2")
li.primero.prox.prox = _Nodo("3")
li.primero.prox.prox.prox = _Nodo("4")
li.primero.prox.prox.prox.prox = _Nodo("5")
li.primero.prox.prox.prox.prox.prox = _Nodo("6")
li.primero.prox.prox.prox.prox.prox.prox = _Nodo("7")
li.primero.prox.prox.prox.prox.prox.prox.prox = _Nodo("8")
print(li)

li.invertir(3)
print(li)