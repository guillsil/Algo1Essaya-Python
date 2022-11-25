"""Implementar un método de Lista Enlazada que asuma que la lista se encuentra ordenada de menor a mayor y
reordene los elementos tal que los deje de forma piramidal. Esto es, tenga una primer sección creciente y
luego una sección decreciente. Qué elementos quedan de cada lado no es importante.

Ejemplo: le = [1,2,3,4,5,6,7] -> [1,3,5,7,6,4,2]"""

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.cant = 0
    def __iter__(self):
        nodo = self.prim
        while nodo:
            yield nodo.dato
            nodo = nodo.prox

    def __str__(self):
        return str(list(self))

    def insertar(self, dato):
        self.prim = _Nodo(dato, self.prim)
        self.cant += 1

    def ordenar_piramidal(self):
        """Reordena los elementos tal que los deje de forma piramidal. Esto es, tenga una primer sección creciente y
        luego una sección decreciente. Qué elementos quedan de cada lado no es importante."""







le = ListaEnlazada()
le.insertar(7)
le.insertar(6)
le.insertar(5)
le.insertar(4)
le.insertar(3)
le.insertar(2)
le.insertar(1)
print(le)
le.ordenar_piramidal()
print(le)

