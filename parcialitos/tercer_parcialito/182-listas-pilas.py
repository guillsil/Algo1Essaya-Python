"""Dada una clase ListaEnlazada con referencia al primer nodo, escribir un método que modifique la lista para que invierta el orden de cada k elementos por grupo, donde k > 0.

Por ejemplo, para la lista:

1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8

Con k = 3, debe modificarse para que quede:

3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7

Con k = 4, debe modificarse para que quede:

4 -> 3 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5

Se permite el uso de Pilas y Colas como estructuras auxiliares.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def __str__(self):
        if self.primero is None:
            return "[]"
        else:
            string = "["
            actual = self.primero
            while actual is not None:
                string += str(actual.valor) + ", "
                actual = actual.proximo
            return string[:-2] + "]"
    def invertirPorGrupo(self, k):
        if self.primero is None:
            raise Exception("La lista está vacía")
        if k <= 1:
            raise Exception("El valor de k debe ser mayor a 1")
        
        pila = []
        cola = []
        nodo_atual = self.primero
        
    