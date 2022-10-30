"""Agregar a ListaEnlazada un método extend que reciba una ListaEnlazada y
agregue a la lista actual los elementos que se encuentran en la lista recibida."""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.prox = None
        self.len = 0
    def extend(self, lista):
        actual = self.primero
        while actual.siguiente != None:
            actual = actual.siguiente
        actual.siguiente = lista.primero

mi_lista = ListaEnlazada()
mi_nodo1 = Nodo(1)
mi_nodo2 = Nodo(2)
mi_nodo3 = Nodo(3)
mi_nodo4 = Nodo(4)
mi_nodo5 = Nodo(5)

mi_lista.primero = mi_nodo1
mi_nodo1.siguiente = mi_nodo2
mi_nodo2.siguiente = mi_nodo3
mi_nodo3.siguiente = mi_nodo4
mi_nodo4.siguiente = mi_nodo5

mi_lista2 = ListaEnlazada()
mi_nodo6 = Nodo(6)
mi_nodo7 = Nodo(7)
mi_nodo8 = Nodo(8)
mi_nodo9 = Nodo(9)
mi_nodo10 = Nodo(10)

mi_lista2.primero = mi_nodo6
mi_nodo6.siguiente = mi_nodo7
mi_nodo7.siguiente = mi_nodo8
mi_nodo8.siguiente = mi_nodo9
mi_nodo9.siguiente = mi_nodo10

mi_lista.extend(mi_lista2)
print(mi_lista)





