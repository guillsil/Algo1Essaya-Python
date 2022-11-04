"""Una lista circular es una lista cuyo último nodo está ligado al primero, de modo
que es posible recorrerla infinitamente. Escribir la clase ListaCircular, incluyendo los méto-
dos insert, append, remove y pop."""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class ListaCircular:
    def __init__(self):
        self.primero = None
        self.prox = None
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
    def pop(self, i=None):
        if i is None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")
        if i == 0:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
        else:
            #buscar los nodos en las pocisiones i-1 e i
            anterior = self.primero
            actual = anterior.siguiente
            for pos in range(1, i):
                anterior = actual
                actual = anterior.siguiente
        #guardar el dato y desenlazar el nodo
        dato = actual.dato
        anterior.siguiente = actual.siguiente

        self.len -= 1
        return dato
    def remove(self, x):
        #borra la primera aparición de x en la lista
        #si no está, levanta ValueError
        if self.primero is None:
            raise ValueError(f"{x} is not in list")
        if self.primero.dato == x:
            self.primero = self.primero.siguiente
        else:
            anterior = self.primero
            actual = anterior.siguiente
            while actual is not None and actual.dato != x:
                anterior = actual
                actual = anterior.siguiente
            if actual is None:
                raise ValueError(f"{x} is not in list")
            #descartar el nodo
            anterior.siguiente = actual.siguiente
        self.len -= 1

    def insert(self, i, x):
        if i < 0 or i > self.len:
            raise IndexError("Índice fuera de rango")
        nuevo = _Nodo(x)
        if i == 0:
            if self.primero is None:
                self.primero = nuevo
                nuevo.prox = nuevo
            else:
                nuevo.prox = self.primero
                self.primero = nuevo
        else:
            anterior = self.primero
            actual = anterior.prox
            for pos in range(1, i):
                anterior = actual
                actual = anterior.prox
            anterior.prox = nuevo
            nuevo.prox = actual
        self.len += 1

mi_lista = ListaCircular()
mi_lista.insert(0, 1)
mi_lista.insert(1, 2)
mi_lista.insert(2, 3)
mi_lista.insert(3, 4)
mi_lista.insert(4, 5)
mi_lista.insert(5, 6)
mi_lista.insert(6, 7)

print(mi_lista)

mi_lista.pop(0)
print(mi_lista)

