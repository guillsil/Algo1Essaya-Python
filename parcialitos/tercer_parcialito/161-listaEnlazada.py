"""Para una implementación de una ListaEnlazada que posee únicamente una referencia al primer nodo, se pide implementar una nueva primitiva que modifique la lista de tal forma que el menor elemento se encuentre al comienzo de la misma, manteniendo el orden relativo del resto de los elementos.

Importante: El método no debe recorrer la lista más de una vez.

Ejemplos:

3 -> 5 -> 4 -> 2 -> 1   =>   1 -> 3 -> 5 -> 4 -> 2
5 -> 6 -> 2 -> 3 -> 7   =>   2 -> 5 -> 6 -> 3 -> 7
3 -> 4 -> 5 -> 6 -> 7   =>   3 -> 4 -> 5 -> 6 -> 7

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
    
    def insertarPrimerElemento(self):
        if self.primero is None:
            raise Exception("La lista está vacía")
        
        nodo_minimo = self.primero
        nodo_actual = self.primero.proximo
        
        while nodo_actual is not None:
            if nodo_actual.valor < nodo_minimo.valor:
                nodo_minimo = nodo_actual
            nodo_actual = nodo_actual.proximo
           
        nodo_minimo.valor, self.primero.valor = self.primero.valor, nodo_minimo.valor

lista = ListaEnlazada()
lista.primero = Nodo(3)
lista.primero.proximo = Nodo(5)
lista.primero.proximo.proximo = Nodo(4)
lista.primero.proximo.proximo.proximo = Nodo(2)
lista.primero.proximo.proximo.proximo.proximo = Nodo(1)
print(lista)

lista.insertarPrimerElemento()
print(lista)


       
    
           
       
    
        