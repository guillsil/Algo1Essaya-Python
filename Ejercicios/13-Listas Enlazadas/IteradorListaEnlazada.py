class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
class IteradorListaEnlazada:
    """Almacena el estado de una iteración sobre la ListaEnlazada."""
    def __init__(self, lista):
        """Crea un iterador para la lista dada"""
        self.lista = lista
        self.anterior = None
        self.actual = lista.prim
    def avanzar(self):
        """Avanza la iteración un paso hacia adelante.
        Pre: la iteración no debe haber llegado al final.
        """
        self.anterior = self.actual
        self.actual = self.actual.prox
    def dato_actual(self):
        """Devuelve el elemento en la posición actual de iteración.
        Pre: la iteración no debe haber llegado al final.
        """
        return self.actual.dato
    def esta_al_final(self):
        """Devuelve verdadero si la iteración llegó al final de la lista."""
        return self.actual is None

    def insertar(self, x):
        """Insertar un elemento en el lugar de la iteración actual.
        Una vez insertado, el nuevo elemento será el actual de la iteración,
        y el elemento que antes era el actual será el siguiente.
        """
        nuevo = _Nodo(x)
        if self.anterior:
            nuevo.prox = self.anterior.prox
            self.anterior.prox = nuevo
         else:
             nuevo.prox = self.lista.prim
             self.lista.prim = nuevo
        self.actual = nuevo

        def eliminar(self):
            dato = self.dato_actual()
            if self.anterior:
                self.anterior.prox = self.actual.prox
                self.actual = self.anterior.prox
            else:
                self.lista.prim = self.actual.prox
                self.actual = self.lista.prim
                return dato
