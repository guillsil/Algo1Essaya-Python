"""Escribir un método recursivo de LE que reciba una funcion f y devuelva una nueva lista enlazada que contiene al principio todos los elementos para los que f devuelve True, y luego todos los elementos para los que f devuelve False. No es necesario mantener el orden relativo de los elementos en cada grupo. La LE está implementada con únicamente una referencia al primer nodo. No tiene ningun otro atributo, no se pueden utilizar métodos de la clase ni estructura auxiliares, ni recorrer la lista más de una vez.

Ejemplo:

le === 3 -> 2 -> 5 -> 7 -> 8
le.particionar(es_par)
le === 2 -> 8 -> 5 -> 3 -> 7"""

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
    def particionar(self, f):
        if self.primero is None:
            raise Exception("Lista vacia")
        actual = self.primero
        while actual is not None:
            if f(actual.dato):
                nodo = Nodo(actual.dato)
                nodo.siguiente = self.primero
                self.primero = nodo
            else:
                nodo = Nodo(actual.dato)
                nodo.siguiente = self.primero
                self.primero = nodo
            actual = actual.siguiente
        return self.primero