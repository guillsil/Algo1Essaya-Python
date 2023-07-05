"""Implementar el método downsamp(k) para una implementación de ListaEnlazada con referencia úniccamente 
al primer nodo . Este método debe eliminar todo elemento de la lista que ocupe una posición que no sea
múltiple del npumero k pasado por parámetro (k > 1). Ejemplos:
l : [0, 1, 2, 3, 4, 5]                        -> l.downsamp(2) -> l : [0, 2, 4]
l : ["a", "b", "c", "d", "e", "f", "g"]       -> l.downsamp(4) -> l : ["a", "e"]
l : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]           -> l.downsamp(3) -> l : [1, 4, 7, 10]
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
    def downsamp(self, k):
        if self.primero is None:
            raise Exception("Lista Vacia")
        if k < 0:
            raise Exception("k no puede ser menor que 0")
        nodo_actual = self.primero
        nodo_anterior = None 
        indice = 1
        while nodo_actual is not None:
            if k % indice == 0:
                #mantengo el nodo actual 
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            else:
                # Eliminamos el nodo actual
                if nodo_anterior is None:
                    # Si es el primer nodo, actualizamos el puntero al primero
                    self.primero = nodo_actual.siguiente
                    nodo_actual = self.primero
                else:
                    # Si no es el primer nodo, ajustamos los punteros
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    nodo_actual = nodo_actual.siguiente
        indice += 1




