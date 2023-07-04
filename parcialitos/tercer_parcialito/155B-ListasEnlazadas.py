"""Teniendo una ListaEnlazada implementada como solo una referencia al primer nodo, se pide implementar el método __mul__ que reciba un número entero n y devuelva una nueva lista enlazada con los mismos elementos repetidos n veces.

Aclaración: la nueva lista debe ser recorrida una sola vez (es decir, no se puede utilizar el método append().

Ejemplo:

L: [a,b] → L * 3 → [a,b,a,b,a,b]

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
    def __mul__(self, n):
        if self.primero is None:
            raise Exception("La lista está vacía")
        
        nueva_lista = ListaEnlazada()
        actual = self.primero
        for i in range(n):
            while actual is not None:
                nueva_lista.agregar_elemento(actual.dato)
                actual = actual.siguiente
            actual = self.primero
        return nueva_lista
    
    
lista = ListaEnlazada()
lista.agregar_elemento("a")
lista.agregar_elemento("b")

print(lista)
print(lista * 6)
