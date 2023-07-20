class Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
class Pila:
    #implemetacion con nodos
    def __init__(self):
        self.tope = None
    def apilar(self, dato):
        nodo = Nodo(dato, self.tope)
        self.tope = nodo
    def desapilar(self):
        #elimina el tope de la pila y lo devuelve
        if self.tope is None:
            raise ValueError("La pila esta vacia")
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato
    def ver_tope(self):
        #devuelve el tope de la pila
        if self.tope is None:
            raise ValueError("La pila esta vacia")
        return self.tope.dato
    def esta_vacia(self):
        return self.tope is None
