class Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
class Pila:
    #implemetacion con arreglos
    def __init__(self):
        self.tope = None
        self.datos = []
    def apilar(self, dato):
        self.datos.append(dato)
        self.tope = len(self.datos) - 1
    def desapilar(self):
        #elimina el tope de la pila y lo devuelve
        if self.tope is None:
            raise ValueError("La pila esta vacia")
        dato = self.datos[self.tope]
        self.datos.pop()
        self.tope = len(self.datos) - 1
        return dato
    def ver_tope(self):
        #devuelve el tope de la pila
        if self.tope is None:
            raise ValueError("La pila esta vacia")
        return self.datos[self.tope]
    def esta_vacia(self):
        return self.tope is None