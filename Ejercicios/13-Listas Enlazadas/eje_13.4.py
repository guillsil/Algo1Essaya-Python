"""Implementar el método duplicar(elemento) de ListaEnlazada, que recibe un
elemento y duplica todas las apariciones del mismo. Ejemplo:
L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
L.duplicar(8) => L = 1 -> 5 -> 8 -> 8 -> 8 -> 8 -> 2 -> 8 -> """
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

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
    def duplicar(self, elemento):
        actual = self.primero
        anterior = None
        while actual != None:
            if actual.dato == elemento:
                nuevo = Nodo(elemento)
                nuevo.siguiente = actual.siguiente
                actual.siguiente = nuevo
                anterior = actual
                actual = actual.siguiente
            anterior = actual
            actual = actual.siguiente


mi_lista = ListaEnlazada()
mi_nodo1 = Nodo(1)
mi_nodo2 = Nodo(5)
mi_nodo3 = Nodo(8)
mi_nodo4 = Nodo(8)
mi_nodo5 = Nodo(2)

mi_lista.primero = mi_nodo1
mi_nodo1.siguiente = mi_nodo2
mi_nodo2.siguiente = mi_nodo3
mi_nodo3.siguiente = mi_nodo4
mi_nodo4.siguiente = mi_nodo5

mi_lista.duplicar(5)
print(mi_lista)