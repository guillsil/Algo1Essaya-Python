"""Se tiene una clase ListaEnlazada cuya implementación cuenta únicamente con una referencia al primer nodo, que contiene números ordenados de forma ascendente. Se pide escribir un método de la clase ListaEnlazada que la modifique eliminando sus elementos repetidos. No se pueden utilizar otros métodos de la lista ni estructuras auxiliares."""
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
    def elimiarRepetidos(self):
        if self.primero is None:
            raise Exception("Lista vacia")
        actual = self.primero
        while actual.siguiente is not None:
            if actual.dato == actual.siguiente.dato:
                actual.siguiente = actual.siguiente.siguiente
            else:
                actual = actual.siguiente

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(2)
lista.agregar_elemento(3)

print(lista)
lista.elimiarRepetidos()
print(lista)