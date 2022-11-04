"""Implementar el método filter(f) de ListaEnlazada, que recibe una función y
devuelve una nueva lista enlazada con los elementos para los cuales la aplicación de f devuelve
True. La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se
puede llamar a append). Ejemplo:
L = 1 -> 5 -> 8 -> 8 -> 2 -> 8
L.filter(es_primo) -> L2 = 5 -> 2"""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.prox = None
        self.len = 0
    def __str__(self):
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(str(actual.dato))
            actual = actual.siguiente
        return f"Lista Enlazada({', '.join(lista)})"

    def append(self, dato):
        if self.esta_vacia():
            self.primero = self.prox = _Nodo(dato)
        else:
            self.prox.siguiente = _Nodo(dato)
            self.prox = self.prox.siguiente
        self.len += 1
    def filter(self, f):
        actual = self.primero
        lista = ListaEnlazada()
        # La nueva lista debe ser construida recorriendo los nodos una sola vez (es decir, no se puede llamar a append)
        while actual != None:
            if f(actual.dato):
                lista.append(actual.dato)
            actual = actual.siguiente
        return lista

    def esta_vacia(self):
        return self.primero == None

def es_primo(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

mi_lista = ListaEnlazada()
mi_nodo1 = _Nodo(1)
mi_nodo2 = _Nodo(5)
mi_nodo3 = _Nodo(8)
mi_nodo4 = _Nodo(8)
mi_nodo5 = _Nodo(2)

mi_lista.primero = mi_nodo1
mi_nodo1.siguiente = mi_nodo2
mi_nodo2.siguiente = mi_nodo3
mi_nodo3.siguiente = mi_nodo4
mi_nodo4.siguiente = mi_nodo5


print(mi_lista.filter(es_primo))