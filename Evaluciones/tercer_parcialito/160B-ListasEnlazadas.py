"""Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva. Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0. La implementación de LE contiene una referencia al primer nodo y un atributo con la longitud. Ejemplo: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (len = 8)

le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]

"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0

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
    def __len__(self):
        return self.len
    def rotar(self, n):
        
        nodo_actual = self.primero
        nodo_aux = None
        while n > 0:
            nodo_aux = nodo_actual
            nodo_actual = nodo_actual.siguiente
            n -= 1
        nodo_aux.siguiente = None
        nodo_aux = nodo_actual
        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente 
        nodo_actual.siguiente = self.primero
        self.primero = nodo_aux
        return self
    
le = ListaEnlazada()
le.agregar_elemento(1)
le.agregar_elemento(3)
le.agregar_elemento(3)
le.agregar_elemento(4)

print(le)
le.rotar(2)
print(le)


    
        