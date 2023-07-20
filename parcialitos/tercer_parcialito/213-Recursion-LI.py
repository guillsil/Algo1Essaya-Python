"""Escribir un método recursivo de LE que reciba una funcion f y devuelva una nueva lista enlazada que contiene
al principio todos los elementos para los que f devuelve True, y luego todos los elementos para los que f
devuelve False. No es necesario mantener el orden relativo de los elementos en cada grupo. La LE está implementada
con únicamente una referencia al primer nodo. No tiene ningun otro atributo, no se pueden utilizar métodos de la
clase ni estructura auxiliares, ni recorrer la lista más de una vez.
Ejemplo:
le === 3 -> 2 -> 5 -> 7 -> 8
le.particionar(es_par)
le === 2 -> 8 -> 5 -> 3 -> """

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class  ListaEnlazada:
    def __init__(self):
        self.prim = None

    def __iter__(self):
        nodo = self.prim
        while nodo:
            yield nodo.dato
            nodo = nodo.prox

    def __str__(self):
        return " -> ".join(str(dato) for dato in self)

    def insertar(self, dato):
        self.prim = _Nodo(dato, self.prim)

    def particionar(self, f):
        if self.prim is None:
            return
        if self.prim.prox is None:
            return
        if f(self.prim.dato):
            self.prim = self.prim.prox
            self.particionar(f)
        else:
            self.prim = self.prim.prox
            self.particionar(f)
            self.prim = self.prim.prox






le = ListaEnlazada()
le.insertar(8)
le.insertar(7)
le.insertar(5)
le.insertar(2)
le.insertar(3)
print(le)
le.particionar(lambda x: x % 2 == 0)
print(le)

