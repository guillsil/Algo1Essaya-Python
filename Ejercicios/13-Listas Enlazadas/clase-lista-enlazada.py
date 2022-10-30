#Construcción de la lista Enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.prox = None
        self.len = 0
    def esta_vacia(self):
        return self.primero == None

    def append(self, dato):
        if self.esta_vacia():
            self.primero = self.prox = Nodo(dato)
        else:
            self.prox.siguiente = Nodo(dato)
            self.prox = self.prox.siguiente
        self.len += 1

    def __len__(self):
        return self.len

    def __iter__(self):
        actual = self.primero
        while actual != None:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        return f"ListaEnlazada({', '.join(str(dato) for dato in self)})"

    def __repr__(self):
        return str(self)

    def pop(self, i=None):
        if i == None:
            i = self.len - 1
        if i < 0 or i >= self.len:
            raise IndexError("pop index out of range")
        if i == 0:
            dato = self.primero.dato
            self.primero = self.primero.siguiente
        else:
            anterior = self.primero
            for j in range(i-1):
                anterior = anterior.siguiente
            dato = anterior.siguiente.dato
            anterior.siguiente = anterior.siguiente.siguiente
        self.len -= 1
        return dato

    def remove(self, x):
        if self.primero is None:
            raise ValueError(f"{x} is not in list")
        if self.primero.dato == x:
            self.primero = self.primero.siguiente
        else:
            anterior = self.primero
            while anterior.siguiente != None and anterior.siguiente.dato != x:
                anterior = anterior.siguiente
            if anterior.siguiente == None:
                raise ValueError(f"{x} not in list")
            anterior.siguiente = anterior.siguiente.siguiente
        self.len -= 1
    def insert(self, i, x):
        if i < 0 or i > self.len:
            raise IndexError("list index out of range")
        if i == 0:
            self.primero = Nodo(x, self.primero)
        else:
            anterior = self.primero
            for j in range(i-1):
                anterior = anterior.siguiente
            anterior.siguiente = Nodo(x, anterior.siguiente)
        self.len += 1
    def index(self, x):
        anterior = self.primero
        for i in range(self.len):
            if anterior.dato == x:
                return i
            anterior = anterior.siguiente
        raise ValueError(f"{x} not in list")