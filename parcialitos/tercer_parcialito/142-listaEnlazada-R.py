"""Implementar el método swap para una implementación de ListaEnlazada con referencia únicamente al primer nodo.
Éste recibe dos números positivos que representan posiciones y debe modificar la lista intercambiando los valores
ubicados en dichas posiciones. En caso de que los índices recibidos por parámetro excedan la longitud de la lista,
se debe lanzar una excepción del tipo IndexError. Ejemplo: Si L es [1,3,2,6,4], L.swap(1,3) dejará la lista como
[1,6,2,3,4]."""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.prox
        return f"Lista Enlazada({', '.join(lista)})"
    def swap(self, i, j):
        """Implementar el método swap para una implementación de ListaEnlazada con referencia únicamente al primer nodo."""
        if i == j:
            return
        # i siempre va a ser menor que j
        if i > j:
            i, j = j, i
        actual = self.primero
        len = 0
        while actual is not None:
            actual = actual.prox
            len += 1
        if i >= len or j >= len:
            raise IndexError
        actual = self.primero
        for k in range(len):
            if k == i:
                dato_i = actual.dato
            if k == j:
                dato_j = actual.dato
            actual = actual.prox
        actual = self.primero
        for k in range(len):
            if k == i:
                actual.dato = dato_j
            if k == j:
                actual.dato = dato_i
            actual = actual.prox
        return

li = ListaEnlazada()
li.primero = _Nodo(1)
li.primero.prox = _Nodo(3)
li.primero.prox.prox = _Nodo(2)
li.primero.prox.prox.prox = _Nodo(6)
li.primero.prox.prox.prox.prox = _Nodo(4)
print(li)
li.swap(1,3)
print(li)