"""Implementar para la ListaEnlazada el método distribuir_en_colas(k), que recibe por parámetro un número entero k mayor a 1. Este nuevo método debe devolver k nuevas colas con los elementos de la lista distribuidos de forma alternada, respetando el orden relativo de los elementos (los k elementos que están al principio de la lista quedarían al frente de cada una de las colas). Ejemplos:

L = [a b c d e f g] → L.distribuir(3) → [Cola([a d g]), Cola([b e]), Cola([c f])]
L = [a b c] → L.distribuir(4) → [Cola([a]), Cola([b]), Cola([c]), Cola([])]

"""
from cola import Cola
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
    def distribuir(self, k):
        if self.primero is None:
            raise Exception("Lista vacía")
        if k < 1:
            raise Exception("k debe ser mayor a 1")
        nodo_actual = self.primero
        nueva_lista = ListaEnlazada()
        colas = []
        indice = 0
        for i in range(k):
            colas.append(Cola())
        while nodo_actual is not None:
            colas[indice].encolar(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
            indice = (indice + 1) % k
        for cola in colas:
            nueva_lista.agregar_elemento(cola)
        return nueva_lista
    
        

        

lista = ListaEnlazada()
lista.agregar_elemento("a")
lista.agregar_elemento("b")
lista.agregar_elemento("c")
lista.agregar_elemento("d")
lista.agregar_elemento("e")

print(lista)

nueva_lista = lista.distribuir(3)

actual = nueva_lista.primero
while actual is not None:
    cola = actual.dato
    print(cola)
    actual = actual.siguiente
    