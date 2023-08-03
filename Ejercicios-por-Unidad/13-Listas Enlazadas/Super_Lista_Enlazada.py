"""Escribir la clase lista enlazada, usando la clase nodo vista en clase. La clase lista enlazada debe tener los siguientes métodos:"""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.prox
        return f"Lista Enlazada({', '.join(lista)})"
    def __len__(self):
        return self.len
    def __iter__(self):
        self.actual = self.primero
        return self
    def append(self, x):
        #agrega el elemento x al final de la lista
        nuevo = _Nodo(x)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.prox is not None:
                actual = actual.prox
            actual.prox = nuevo
        self.len += 1
    def insert(self, i, x):
        #inserta el elemento x en la posición i
        if i < 0 or i > self.len:
            raise IndexError("Índice fuera de rango")
        nuevo = _Nodo(x)
        if i == 0:
            nuevo.prox = self.primero
            self.primero = nuevo
        else:
            anterior = self.primero
            for pos in range(1, i):
                actual = anterior.prox
            nuevo.prox = anterior.prox
            anterior.prox = nuevo
        self.len += 1


    def pop(self, i=None):
        #saca el elemento de la posición i
        #si no se pasa i, saca el último
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.primero.dato
            self.primero = self.primero.prox
        else:
            #buscar los nodos en las pocisiones i-1 e i
            anterior = self.primero
            actual = anterior.prox
            for pos in range(1, i):
                anterior = actual
                actual = anterior.prox
        #guardar el dato y desenlazar el nodo
        dato = actual.dato
        anterior.prox = actual.prox

        self.len -= 1
        return dato

    def remove(self, x):
        """Elimina la primera aparición del elemento x de la lista"""
        if self.primero is None:
            raise ValueError("El elemento no está en la lista")
        if self.primero.dato == x:
            self.primero = self.primero.prox
            return
        anterior = self.primero
        actual = anterior.prox
        while actual is not None and actual.dato != x:
            anterior = actual
            actual = anterior.prox
        if actual is None:
            raise ValueError("El elemento no está en la lista")
        anterior.prox = actual.prox
        self.len -= 1

    def shift(self, n):
        """Elimina los primeros n elementos de la lista y devuelve una nueva lista con dichos elementos"""
        if n <= 0:
            return ListaEnlazada()
        if self.primero is None:
            return ListaEnlazada()
        actual = self.primero
        for i in range(n-1):
            if actual.prox is None:
                break
            actual = actual.prox
        nueva = ListaEnlazada()
        nueva.primero = self.primero
        self.primero = actual.prox
        actual.prox = None
        return nueva
