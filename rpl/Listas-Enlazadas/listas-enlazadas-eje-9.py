"""Una lista doblemente enlazada es una lista en la cual cada nodo tiene una referencia al anterior además de
al próximo de modo que es posible recorrerla en ambas direcciones.

Escribir la clase ListaDobleEnlazada con el método append(x), que agrega el elemento x al final de la lista.

Nota: A la clase _Nodo se le incluye un nuevo atributo ant

Extra: ¿Cómo serían las implementaciones de pop(i), insert(i, x) y remove(x)?"""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
        self.ant = None
class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.len = 0
    def append(self, x):
        #agrega el elemento x al final de la lista
        if self.primero is None:
            self.primero = _Nodo(x)
        #buscar el último nodo
        else:
            actual = self.primero
            while actual.prox != None:
                actual = actual.prox
            actual.prox = _Nodo(x)
            actual.prox.ant = actual
        self.len += 1