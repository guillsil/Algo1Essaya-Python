"""Intercambiar nodos en Lista Enlazada: Implementa el método intercambiar_nodos(pos1, pos2) para
la clase ListaEnlazada que intercambie los nodos ubicados en las posiciones pos1 y pos2.
Por ejemplo:
lista = ListaEnlazada([1, 2, 3, 4, 5, 6, 7, 8, 9])
lista.intercambiar_nodos(1, 3)
lista.imprimir() # imprime 1 4 3 2 5 6 7 8 9
"""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def intercambiar_nodos(self, pos1, pos2):
        if self.prim is None:
            raise ValueError("La lista esta vacia")
        if pos1 > self.len or pos2 > self.len:
            raise IndexError("Posicion fuera de rangi")
        if pos1 == pos2:
            return self
        if pos2 < pos1:
            pos1, pos2 = pos2, pos1

        actual = self.prim

        for i in range(self.len):
            if i == pos1:
                nodo1 = actual
            if i == pos2:
                nodo2 = actual
            actual = actual.prox

        nodo1.dato, nodo2.dato = nodo2.dato, nodo1.dato
        return self

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
print(lista.intercambiar_nodos(1, 3))

"""Multiplicar elementos en Lista Enlazada: Implementa el método multiplicar_elementos(x, N) para la
clase ListaEnlazada, que modifique la lista enlazada de tal forma que los elementos iguales a x de la
misma se vean duplicados N veces. No es necesario iterar la lista más de una vez.
Ejemplo:
l = ListaEnlazada([6, 8, 6, 5, 5])
l.multiplicar_elementos(6, 3)
l.imprimir() # imprime 6 6 6 8 6 6 6 5 5 5 5 5
"""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def multiplicar_elementos(self, x, n):
        if self.prim is None:
            raise Exception("La lista esta Vacia")
        if n == 0:
            return self

        actual = self.prim

        while actual is not None:
            if actual.dato == x:
                for i in range(n-1):
                    nodo = Nodo(x, actual.prox)
                    actual.prox = nodo
                    actual = actual.prox
            actual = actual.prox
        return self

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
print(lista.multiplicar_elementos(6, 3))

"""Método shift para ListaEnlazada: Implementa el método shift(n) para una implementación de ListaEnlazada
con referencia únicamente al primer nodo. Este método debe eliminar los primeros n elementos y devolver
una nueva ListaEnlazada con dichos elementos eliminados. El método no debe recorrer la lista más de una
vez ni utilizar otro método de la clase ListaEnlazada.
Ejemplo:
le = ListaEnlazada([4, 5, 2, 5, 7])
nueva_lista = le.shift(2)
# Después de llamar al método, le = 2 -> 5 -> 7 y nueva_lista = 4 -> 5
"""

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def shift(self, n):
        if self.prim is None:
            raise Exception("La lista esta vacia")

        actual = self.prim
        nueva_lista = ListaEnlazada()

        for i in range(n):
            nueva_lista.agregar(actual.dato)
            actual = actual.prox

        self.prim = actual
        return nueva_lista

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
print(lista.shift(2))


"""Distribuir en Colas: Implementa el método distribuir_en_colas(k) para una implementación de ListaEnlazada con
referencia únicamente al primer nodo. Este método debe devolver k nuevas colas con los elementos de la lista
distribuidos de forma alternada, respetando el orden relativo de los elementos.
Ejemplos:
L = ListaEnlazada(["a", "b", "c", "d", "e", "f", "g"])
colas = L.distribuir_en_colas(3)
# Debe devolver: [Cola(["a", "d", "g"]), Cola(["b", "e"]), Cola(["c", "f"])]

L = ListaEnlazada([1, 2, 3])
colas = L.distribuir_en_colas(4)
# Debe devolver: [Cola([1]), Cola([2]), Cola([3]), Cola([])]
"""
from cola import Cola
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def distribuir_en_colas(self, k):
        if self.prim is None:
            raise Exception("La lista esta vacia")

        colas = []
        for i in range(k):
            colas.append(Cola())

        actual = self.prim
        i = 0
        while actual is not None:
            colas[i].encolar(actual.dato)
            i += 1
            if i == k:
                i = 0
            actual = actual.prox
        return colas

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
colas = lista.distribuir_en_colas(3)
for cola in colas:
    print(cola)
print(len(colas))

"""Inversión de k Nodos en Grupos: Dada una clase ListaEnlazada con referencia al primer nodo, implementa un método
que modifique la lista para que invierta el orden de cada k elementos por grupo, donde k > 0.
Ejemplos:
le = ListaEnlazada([1, 2, 3, 4, 5, 6, 7, 8])
le.invertir_grupos(3)
# Después de llamar al método, le = 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7

le = ListaEnlazada([1, 2, 3, 4, 5, 6, 7, 8])
le.invertir_grupos(4)
# Después de llamar al método, le = 4 -> 3 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5
"""
from pila import Pila

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def invertir_grupos(self, k):
        pila = Pila()
        if self.prim is None:
            raise Exception("La lista esta vacia")
        if k == 0:
            return self

        actual = self.prim
        nueva_lista = ListaEnlazada()

        while actual is not None:
            for i in range(k):
                pila.apilar(actual.dato)
                actual = actual.prox
                if actual is None:
                    break
            while not pila.esta_vacia():
                nueva_lista.agregar(pila.desapilar())
        return nueva_lista

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
print(lista.invertir_grupos(3))

"""Eliminar Elementos entre Índices: Implementa el método chop(i, j) para la clase ListaEnlazada que modifique la lista de
tal forma que elimine todos los elementos que se encuentren entre los índices i (inclusive) y j (exclusive).
Si algún índice se va de rango de la lista, se considera el inicio o el final de la lista según corresponda.
Si i >= j, el método no hace nada. El método no debe recorrer la lista más de una vez ni utilizar estructuras auxiliares.
Ejemplo:
le = ListaEnlazada([1, 5, 3, 4, 6])
le.chop(1, 3)
# Después de llamar al método, le = 1 -> 4 -> 6"""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada():
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

    def chop(self, i, j):
        if self.prim is None:
            raise Exception("La lista esta vacia")
        if i >= j:
            return self
        if j > self.len:
            j = self.len
        if i > self.len:
            i = 0

        actual = self.prim

        for k in range(self.len):
            if k == i-1:
                nodo1 = actual
            if k == j:
                nodo2 = actual
            actual = actual.prox

        nodo1.prox = nodo2
        return self
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(6)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
print(lista.chop(1, 3))






