"""Dada una lista enlazada que únicamente cuenta con una referencia al primer nodo, implementar para la misma el
método chop(i, j), que la modifica de tal forma que elimine todos los elementos que se encuentren entre los
índices i (inclusive) y j (exclusive). Si algún índice se va de rango de la lista, se considera el inicio o el
final de la lista según corresponda. Si i >= j, el método no hace nada. El método no debe recorrer la lista más
de una vez ni utilizar estructuras auxiliares. Ejemplos:
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(1, 4)    ==>  le == 1 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(-1, 1)   ==>  le == 5 -> 3 -> 4 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(0, 2)    ==>  le == 3 -> 4 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(1, 7)    ==>  le == 1
"""
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

    def chop(self, i, j):
        """Elimina los elementos entre los índices i (inclusive) y j (exclusive)"""
        if i >= j:
            return
        if self.primero is None:
            return
        actual = self.primero
        anterior = None
        # Busco el nodo anterior al que voy a eliminar
        for k in range(i):
            if actual.prox is None:
                break
            anterior = actual
            actual = actual.prox
        # Si anterior es None, entonces el nodo a eliminar es el primero
        if anterior is None:
            self.primero = actual.prox
            actual.prox = None
            actual = self.primero
        # Si anterior no es None, entonces el nodo a eliminar es el siguiente al anterior
        else:
            anterior.prox = actual.prox
            actual.prox = None
            actual = anterior.prox
        # Elimino los nodos entre i y j
        for k in range(j-i-1):
            if actual.prox is None:
                break
            actual = actual.prox
        # Si actual es None, entonces no hay más nodos que eliminar
        if actual is None:
            return
        # Si actual no es None, entonces el nodo a eliminar es el siguiente al anterior
        else:
            anterior.prox = actual.prox
            actual.prox = None










li = ListaEnlazada()
li.primero = _Nodo(1)
li.primero.prox = _Nodo(5)
li.primero.prox.prox = _Nodo(3)
li.primero.prox.prox.prox = _Nodo(4)
li.primero.prox.prox.prox.prox = _Nodo(6)
print(li)

li.chop(1, 4)
print(li)