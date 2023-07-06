"""Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva.
Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0.

La implementación de LE contiene una referencia al primer nodo (self.prim) y un atributo con la longitud (self.cant).
Cada nodo tiene un atributo para el dato dato y el próximo nodo prox.

Ejemplos: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (self.cant = 8)

le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar_elemento(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo

    def __str__(self):
        if self.primero is None:
            return "[]"

        actual = self.primero
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " ".join(elementos) + "]"
    def rotar(self, n):
        if self.primero is None:
            raise Exception("Lista Vacia")
        if n == 0:
            return
        if n > self.cant:
            n = n % self.cant
        if n == self.cant:
            return
        
        nodo_actual = self.primero
        nodo_aux = None
        for i in range(n):
            nodo_aux = nodo_actual
            nodo_actual = nodo_actual.siguiente
        nodo_aux.siguiente = None
        nodo_aux = nodo_actual
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = self.primero
        self.primero = nodo_aux
    

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(5)
lista.agregar_elemento(6)
lista.agregar_elemento(7)
lista.agregar_elemento(8)

"""print(lista)
lista.rotar(2)"""

"""Implementar un método de la clase ListaEnlazada que elimine sobre la misma lista los elementos consecutivos repetidos. La misma está implementada con únicamente una referencia al primer nodo self.prim y cada nodo tiene los atributos para su dato dato y su próximo nodo prox.

Ejemplo:

L: [3 4 4 4 1 4] -> L.eliminar_consecutivos() -> L: [3 4 1 4]"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar_elemento(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo

    def __str__(self):
        if self.primero is None:
            return "[]"

        actual = self.primero
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " ".join(elementos) + "]"
    
    def eleiminar_consecutivos(self):
        if self.primero is None:
            raise Exception("Lista Vacia")
        nodo_actual = self.primero
        nodo_anterior = Nodo(None)
        while nodo_actual is not None:
            if nodo_anterior.dato == nodo_actual.dato:
                nodo_actual = nodo_actual.siguiente
                nodo_anterior.siguiente = nodo_actual
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
        return self.primero
    
lista = ListaEnlazada()
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(4)
lista.agregar_elemento(4)
lista.agregar_elemento(1)
lista.agregar_elemento(4)

print(lista)
lista.eleiminar_consecutivos()
print(lista)
        
