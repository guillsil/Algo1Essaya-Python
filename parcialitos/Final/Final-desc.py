"""Eliminar nodos duplicados: Implementa una función en la clase ListaEnlazada que elimine todos los nodos
duplicados en la lista. Es decir, si hay nodos con el mismo valor, se debe mantener solo uno de ellos,
 eliminando los demás duplicados."""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def __str__(self):
        actual = self.prim
        lista = []
        while actual:
            lista.append(str(actual.dato))
            actual = actual.prox
        return " ".join(lista)

    def agregar(self, dato):
        nodo = Nodo(dato)
        if not self.prim:
            self.prim = nodo
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
            actual.prox = nodo
        self.len += 1

    def eliminar_duplicados(self):
        if self.prim is None:
            raise ValueError("Lista Vacia")
        actual = self.prim
        valores = set()
        valores.add(actual.dato)
        while actual.prox is not None:
            if actual.prox.dato in valores:
                actual.prox = actual.prox.prox
            else:
                valores.add(actual.prox.dato)
                actual = actual.prox
        return self

"""Combinar dos listas ordenadas: Implementa una función que reciba dos listas enlazadas ordenadas de forma 
ascendente y devuelva una nueva lista enlazada que combine ambas en orden ascendente, sin duplicados.
"""

def combinar_listas_ordenadas(lista1, lista2):
     if lista1.prim is None:
        return lista2
    if lista2.prim is None:
        return lista1
    nueva = ListaEnlazada()
    actual1 = lista1.prim
    actual2 = lista2.prim
    while actual1 is not None and actual2 is not None:
        if actual1.dato < actual2.dato:
            nueva.agregar(actual1.dato)
            actual1 = actual1.prox
        elif actual1.dato > actual2.dato:
            nueva.agregar(actual2.dato)
            actual2 = actual2.prox
        else:
            nueva.agregar(actual1.dato)
            actual1 = actual1.prox
            actual2 = actual2.prox
    while actual1 is not None:
        nueva.agregar(actual1.dato)
        actual1 = actual1.prox
    while actual2 is not None:
        nueva.agregar(actual2.dato)
        actual2 = actual2.prox
    return nueva

"""Recorrer lista en sentido inverso: Implementa una función en la clase ListaEnlazada que recorra la lista
enlazada de forma recursiva en sentido inverso, es decir, desde el último nodo hasta el primero.
La función debe imprimir o devolver los valores de los nodos en este orden."""
class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.len = 0

    def __str__(self):
        actual = self.prim
        lista = []
        while actual:
            lista.append(str(actual.dato))
            actual = actual.prox
        return " ".join(lista)

    def agregar(self, dato):
        nodo = Nodo(dato)
        if not self.prim:
            self.prim = nodo
        else:
            actual = self.prim
            while actual.prox:
                actual = actual.prox
            actual.prox = nodo
        self.len += 1
    def recorrer_inverso_aux(self, actual):
        if actual.prox is not None:
            self.recorrer_inverso_aux(actual.prox)
        print(actual.dato)

    def recorrer_inverso(self):
        #recorrer de forma recursiva en sentido inverso
        if self.prim is None:
            return
        self.recorrer_inverso_aux(self.prim)



