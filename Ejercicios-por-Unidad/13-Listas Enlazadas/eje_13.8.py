"""Una lista doblemente enlazada es una lista en la cual cada nodo tiene una refe-
rencia al anterior además de al próximo de modo que es posible recorrerla en ambas direcciones.
Escribir la clase ListaDobleEnlazada, incluyendo los métodos insert, append, remove y pop."""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
        self.ant = None

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
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

    def insert(self, i, x):
        if i < 0 or i > self.len:
            raise IndexError("Índice fuera de rango")
        nuevo = _Nodo(x)
        if i == 0:
            nuevo.prox = self.primero
            self.primero = nuevo
        else:
            anterior = self.primero
            for pos in range(1, i):
                anterior = anterior.prox
            nuevo.prox = anterior.prox
            anterior.prox = nuevo
        self.len += 1
    def append(self, x):
        self.insert(self.len, x)

    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.primero.dato
            self.primero = self.primero.prox
        else:
            anterior = self.primero
            for pos in range(1, i):
                anterior = anterior.prox
            dato = anterior.prox.dato
            anterior.prox = anterior.prox.prox
        self.len -= 1
        return dato

    def remove(self, x):
        if self.primero is None:
            raise ValueError(f"{x} is not in list")
        if self.primero.dato == x:
            self.primero = self.primero.prox
        else:
            anterior = self.primero
            actual = anterior.prox
            while actual is not None and actual.dato != x:
                anterior = actual
                actual = anterior.prox
            if actual is None:
                raise ValueError(f"{x} is not in list")
            anterior.prox = actual.prox
        self.len -= 1
