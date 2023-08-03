"""Implementar el método merge() para una implementación de ListaEnlazada con referencia únicamente al primer nodo. Éste método recibe otra ListaEnlazada por parámetro y tiene como precondición que ambas tienen a todos sus elementos ordenados. El método debe devolver una nueva lista enlazada que contenga a los elementos de las dos en orden. Ejemplos:

L1: [3,5,9], L2: [1,2,6,10] -> [1,2,3,5,6,9,10]

"""
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
    
    def merge(self, otra_lista):
        if self.primero is None:
            raise Exception("Lista vacía")
        if otra_lista.primero is None:
            raise Exception("Lista vacía")
        nodo_actual = self.primero
        otra_actual = otra_lista.primero
        nueva_lista = ListaEnlazada()
        while nodo_actual is not None and otra_actual is not None:
            if nodo_actual.dato < otra_actual.dato:
                nueva_lista.agregar_elemento(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
            elif nodo_actual.dato > otra_actual.dato:
                nueva_lista.agregar_elemento(otra_actual.dato)
                otra_actual = otra_actual.siguiente
            else:
                nueva_lista.agregar_elemento(nodo_actual.dato)
                nodo_actual = nodo_actual.siguiente
                otra_actual = otra_actual.siguiente
        while nodo_actual is not None:
            nueva_lista.agregar_elemento(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        while otra_actual is not None:
            nueva_lista.agregar_elemento(otra_actual.dato)
            otra_actual = otra_actual.siguiente

        return nueva_lista
    
lista = ListaEnlazada()
lista.agregar_elemento(3)
lista.agregar_elemento(5)
lista.agregar_elemento(9)

lista2 = ListaEnlazada()
lista2.agregar_elemento(1)
lista2.agregar_elemento(2)
lista2.agregar_elemento(3)
lista2.agregar_elemento(4)

print(lista)
print(lista2)
print(lista.merge(lista2))
