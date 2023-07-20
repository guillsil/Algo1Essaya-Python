"""Dada una lista enlazada implementada únicamente con una referencia al primer nodo, implementar un método que
reubique el último nodo de la lista en la primera posición."""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

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
    def reubicar_elemento(self):
        """Reubica el último nodo de la lista en la primera posición"""
        if self.primero is None:
            return
        actual = self.primero
        anterior = None
        while actual.prox is not None:
            anterior = actual
            actual = actual.prox
        if anterior is None:
            return
        else:
            anterior.prox = None
            actual.prox = self.primero
            self.primero = actual



li = ListaEnlazada()
li.primero = _Nodo(1)
li.primero.prox = _Nodo(5)
li.primero.prox.prox = _Nodo(3)
li.primero.prox.prox.prox = _Nodo(4)
li.primero.prox.prox.prox.prox = _Nodo(6)
li.primero.prox.prox.prox.prox.prox = _Nodo(5)
print(li)
li.reubicar_elemento()
print(li)
