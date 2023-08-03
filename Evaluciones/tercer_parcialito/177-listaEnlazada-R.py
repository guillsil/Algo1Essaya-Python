"""Implementar para la ListaEnlazada el método distribuir_en_colas(k), que recibe por parámetro un número
entero k mayor a 1. Este nuevo método debe devolver k nuevas colas con los elementos de la lista distribuidos
de forma alternada, respetando el orden relativo de los elementos (los k elementos que están al principio de la
lista quedarían al frente de cada una de las colas). Ejemplos:
L = [a b c d e f g] → L.distribuir(3) → [Cola([a d g]), Cola([b e]), Cola([c f])]
L = [a b c] → L.distribuir(4) → [Cola([a]), Cola([b]), Cola([c]), Cola([])]"""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
class Cola:
    '''Representa a una cola, con operaciones de encolar y
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None
    def __str__(self):
        '''Devuelve el contenido de la cola como una cadena'''
        s = ""
        nodo = self.frente
        while nodo is not None:
            s += str(nodo.dato) + " "
            nodo = nodo.prox
        return s

class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.prox
        return f"Lista Enlazada({', '.join(lista)})"
    def append(self, dato):
        if self.primero is None:
            self.primero = _Nodo(dato)
        else:
            actual = self.primero
            while actual.prox is not None:
                actual = actual.prox
            actual.prox = _Nodo(dato)
    def distribuir_en_colas(self, k):
        """Distribuye los elementos de la lista en k colas, de forma alternada"""
        colas = []
        for i in range(k):
            colas.append(Cola())
        actual = self.primero
        i = 0
        while actual is not None:
            colas[i].encolar(actual.dato)
            actual = actual.prox
            i = (i + 1) % k
        return colas
li = ListaEnlazada()
li.primero = _Nodo("a")
li.primero.prox = _Nodo("b")
li.primero.prox.prox = _Nodo("c")
li.primero.prox.prox.prox = _Nodo("d")
li.primero.prox.prox.prox.prox = _Nodo("e")
li.primero.prox.prox.prox.prox.prox = _Nodo("f")
li.primero.prox.prox.prox.prox.prox.prox = _Nodo("g")
print(li)
print(li.distribuir_en_colas(3))
        