"""Se cuenta con una implementación de ListaEnlazada con únicamente una referencia al primer nodo. Se pide
implementar un método unir_medio, que dada una segunda lista enlazada, la inserte en el medio de la original.

Ejemplo: para las listas a→b→c→d y e→f→g, el resultado debe ser a→b→e→f→g→c→d.

No se puede recorrer ninguna lista más de una vez. Al finalizar la ejecución, la segunda lista debe quedar vacía.
"""
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
    def unir_medio(self, otra):
        """Método unir_medio, que dada una segunda lista enlazada, la inserte en el medio de la original."""
        if self.primero is None:
            self.primero = otra.primero
        if otra.primero is None:
            return
        actual = self.primero
        len =  0
        while actual.prox is not None:
            actual = actual.prox
            len += 1
        actual = self.primero
        #al finalizar la ejecucion otra debe quedar vacia
        for i in range(len):
            if i == len // 2:
                aux = actual.prox
                actual.prox = otra.primero
                actual = actual.prox
                while actual.prox is not None:
                    actual = actual.prox
                actual.prox = aux
                break
            actual = actual.prox
        otra.primero = None









li = ListaEnlazada()
li.primero = _Nodo("a")
li.primero.prox = _Nodo("b")
li.primero.prox.prox = _Nodo("c")
li.primero.prox.prox.prox = _Nodo("f")
li.primero.prox.prox.prox.prox = _Nodo("g")
li.primero.prox.prox.prox.prox.prox = _Nodo("h")
print(li)
li2 = ListaEnlazada()
li2.primero = _Nodo("d")
li2.primero.prox = _Nodo("e")
li2.primero.prox.prox = _Nodo("f")

li.unir_medio(li2)
print(li)
