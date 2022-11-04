class Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
class Cola:
    #con nodos
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def encolar(self, dato):
        nodo = Nodo(dato, None)
        if self.ultimo is not None:
            self.ultimo.prox = nodo
        else:
            self.primero = nodo
        self.ultimo = nodo
    def desencolar(self):
        if self.primero is None:
            raise ValueError("La cola esta vacia")
        dato = self.primero.dato
        self.primero = self.primero.prox
        if self.primero is None:
            self.ultimo = None
        return dato
    def ver_primero(self):
        if self.primero is None:
            raise ValueError("La cola esta vacia")
        return self.primero.dato
    def esta_vacia(self):
        return self.primero is None