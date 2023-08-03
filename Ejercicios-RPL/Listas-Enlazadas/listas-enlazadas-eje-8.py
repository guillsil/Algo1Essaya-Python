"""Una lista circular es una lista cuyo último nodo está ligado al primero, de modo que es posible recorrerla infinitamente.

Escribir la clase ListaCircular con el método append(x), que agrega el elemento x al final de la lista.

Extra: ¿Cómo serían las implementaciones de pop(i), insert(i, x) y remove(x)?"""

class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class ListaCircular:
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

    def append(self, x):
        #agrega el elemento x al final de la lista
        if self.primero is None:
            self.primero = _Nodo(x)
            self.primero.prox = self.primero
        #buscar el último nodo
        else:
            actual = self.primero
            while actual.prox != self.primero:
                actual = actual.prox
            actual.prox = _Nodo(x)
            actual.prox.prox = self.primero
        self.len += 1

    def pop(self, i=None):
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
        #borra la primera aparición de x en la lista
        #si no está, levanta ValueError
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

l1 = ListaCircular()
l1.append(1)
l1.append(2)
l1.append(1)

print(l1)