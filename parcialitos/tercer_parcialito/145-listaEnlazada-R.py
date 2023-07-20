"""Para una implementación de ListaEnlazada con referencia únicamente al primer nodo implementar la primitiva
suma_acumulativa() que devuelva una nueva lista (del mismo largo) tal que el nodo i de la nueva lista contenga
la suma acumulativa de los elementos de la lista original hasta el nodo i.

Por ejemplo: Si lista tiene los elementos 1, 2, 3, 4, lista.suma_acumulativa() devuelve una nueva ListaEnlazada con
1, 3, 6, 10"""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None

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
    def suma_acumulativa(self):
        """Devuelve una nueva lista con la suma acumulativa de los elementos de la lista original"""
        nueva = ListaEnlazada()
        actual = self.primero
        suma = 0
        while actual is not None:
            suma += actual.dato
            nueva.append(suma)
            actual = actual.prox
        return nueva

li = ListaEnlazada()
li.primero = _Nodo(1)
li.primero.prox = _Nodo(5)
li.primero.prox.prox = _Nodo(3)
li.primero.prox.prox.prox = _Nodo(4)
li.primero.prox.prox.prox.prox = _Nodo(6)
li.primero.prox.prox.prox.prox.prox = _Nodo(5)
print(li)
print(li.suma_acumulativa())