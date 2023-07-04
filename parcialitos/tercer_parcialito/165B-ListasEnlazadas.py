"""Dada una lista enlazada que únicamente cuenta con una referencia al primer nodo, implementar para la misma el método chop(i, j), que la modifica de tal forma que elimine todos los elementos que se encuentren entre los índices i (inclusive) y j (exclusive). Si algún índice se va de rango de la lista, se considera el inicio o el final de la lista según corresponda. Si i >= j, el método no hace nada. El método no debe recorrer la lista más de una vez ni utilizar estructuras auxiliares. Ejemplos:

le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(1, 4)    ==>  le == 1 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(-1, 1)   ==>  le == 5 -> 3 -> 4 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(0, 2)    ==>  le == 3 -> 4 -> 6
le = 1 -> 5 -> 3 -> 4 -> 6   ==>  le.chop(1, 7)    ==>  le == 1

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
    
    def chop(self, i, j):
        if i >= j:
            raise ValueError("i debe ser menor a j")
        if i < 0:
            i *= -1
        if j < 0:
            j *= -1
        if self.primero is None:
            raise ValueError("La lista esta vacia")
        
        nodo_actual = self.primero
        contador = 0

        while nodo_actual is not None:
            if contador >= i and contador < j:
                nodo_actual = nodo_actual.siguiente
                contador += 1
            else:
                nodo_actual = nodo_actual.siguiente
                contador += 1
        return self
    
le = ListaEnlazada()
le.agregar_elemento(1)
le.agregar_elemento(5)
le.agregar_elemento(3)
le.agregar_elemento(4)
le.agregar_elemento(6)

print(le)
le.chop(1, 4)
print(le)




