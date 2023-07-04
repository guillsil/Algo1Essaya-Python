"""Implementar un método para una implementación de ListaEnlazada con referencia únicamente al primer nodo que devuelve una nueva lista enlazada compuesta por los elementos que se encuentran en las posiciones impares de la original. Por ejemplo, para L = [3,1,6,8,9] el método debe devolver [1,8]."""
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
    def devolver_impares(self):
        if self.primero is None:
            raise Exception("Lista vacía")
        actual = self.primero
        nueva_lista = ListaEnlazada()
        contador = 1
        while actual is not None:
            if contador % 2 == 0:
                nueva_lista.agregar_elemento(actual.dato)
            contador += 1
            actual = actual.siguiente
        return nueva_lista
    
lista = ListaEnlazada()
lista.agregar_elemento(3)
lista.agregar_elemento(1)
lista.agregar_elemento(6)
lista.agregar_elemento(8)
lista.agregar_elemento(9)

print(lista)

print(lista.devolver_impares())
