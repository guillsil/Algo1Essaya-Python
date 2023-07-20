"""Para una implementación de ListaEnlazada con referencia únicamente al primer nodo implementar la primitiva suma_acumulativa() que devuelva una nueva lista (del mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos de la lista original hasta el nodo i.

Por ejemplo: Si lista tiene los elementos 1, 2, 3, 4, lista.suma_acumulativa() devuelve una nueva ListaEnlazada con 1, 3, 6, 10.
"""
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
    
    def sumaAcumulativa(self):
        if self.primero is None:
            raise Exception("Lista vacía")
        nodo_actual = self.primero
        lista_nueva = ListaEnlazada()
        suma = 0
        while nodo_actual is not None:
            suma += nodo_actual.dato
            lista_nueva.agregar_elemento(suma)
            nodo_actual = nodo_actual.siguiente
        return lista_nueva
    
lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)

print(lista)
print(lista.sumaAcumulativa())

