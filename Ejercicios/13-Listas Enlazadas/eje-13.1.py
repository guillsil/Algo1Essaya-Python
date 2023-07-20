"""Implementar el método __str__ de ListaEnlazada, para que se genere una
salida legible de lo que contiene la lista, similar a las listas de python."""
class Nodo:
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

mi_lista = ListaEnlazada()
mi_nodo1 = Nodo(1)
mi_nodo2 = Nodo(2)
mi_nodo3 = Nodo(3)
mi_nodo4 = Nodo(4)
mi_nodo5 = Nodo(5)
mi_nodo6 = Nodo(6)
mi_nodo7 = Nodo(7)
mi_nodo8 = Nodo(8)
mi_nodo9 = Nodo(9)
mi_nodo10 = Nodo(10)
mi_lista.primero = mi_nodo1
mi_nodo1.siguiente = mi_nodo2
mi_nodo2.siguiente = mi_nodo3
mi_nodo3.siguiente = mi_nodo4
mi_nodo4.siguiente = mi_nodo5
mi_nodo5.siguiente = mi_nodo6
mi_nodo6.siguiente = mi_nodo7
mi_nodo7.siguiente = mi_nodo8
mi_nodo8.siguiente = mi_nodo9
mi_nodo9.siguiente = mi_nodo10
print(mi_lista)


