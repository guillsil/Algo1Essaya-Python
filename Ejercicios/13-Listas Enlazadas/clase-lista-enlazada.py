#Construcción de la lista Enlazada
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

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
        """Inserta el elemento x en la posición i"""
        if i < 0 or i > self.len:
            raise IndexError("list index out of range")
        nuevo = _Nodo(x)
        if i == 0:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            anterior = self.primero
            for pos in range(1, i):
                anterior = anterior.siguiente
            # Insertar el nuevo nodo
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo
        self.len += 1

    def esta_vacia(self):
        return self.primero == None
    def append(self, dato):
        if self.esta_vacia():
            self.primero = self.prox = _Nodo(dato)
        else:
            self.prox.siguiente = _Nodo(dato)
            self.prox = self.prox.siguiente
        self.len += 1
    def __iter__(self):
        actual = self.primero
        while actual != None:
            yield actual.dato
            actual = actual.siguiente

    def __repr__(self):
        return str(self)

    def index(self, x):
        anterior = self.primero
        for i in range(self.len):
            if anterior.dato == x:
                return i
            anterior = anterior.siguiente
        raise ValueError(f"{x} not in list")