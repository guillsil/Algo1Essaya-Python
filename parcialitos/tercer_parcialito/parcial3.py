"""Se cuenta con lista de Lista Enlazada que cuenta unicamente con una referencia al primer elemento.
Escribir el método shiff(n) que elimina sus primeros n elementos y devuelve una nueva LISTA ENLAZADA con dichos elementos
eliminados . El método no debe recorrer listas mas de una vez, ni utilizar otro metodo de la clase ListaEnlazada.
Por ejemplo: para la lista le = 4 => 5 => 2 => 5 => 7
*) le.shift(2) modifica a  le = 2 => 5 => 7=> y devuelve  4 => 5
*) le.shift(3) modifica a  le = 5 => 7=> y devuelve  4 => 5 => 2
*) le.shift(4) modifica a  le = 7=> y devuelve  4 => 5 => 2 => 5
*) le.shift(0) modifica a  le = 4 => 5 => 2 => 5 => 7=> y devuelve una ListaEnlazada vacia
*) le.shift(8) modifica a  le =  y devuelve  4 => 5 => 2 => 5 => 7
"""
class _Nodo:
    """Representa un nodo de una lista enlazada"""
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

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

    def shift(self, n):
        """Elimina los primeros n elementos de la lista y devuelve una nueva lista con dichos elementos"""
        if n <= 0:
            return ListaEnlazada()
        if self.primero is None:
            return ListaEnlazada()
        actual = self.primero
        for i in range(n-1):
            if actual.prox is None:
                break
            actual = actual.prox
        nueva = ListaEnlazada()
        nueva.primero = self.primero
        self.primero = actual.prox
        actual.prox = None
        return nueva

li = ListaEnlazada()
li.primero = _Nodo(4, _Nodo(5, _Nodo(2, _Nodo(5, _Nodo(7)))))
"""print(li.shift(2))"""

"""Escribir una funcion que reciba una cola y un elemento E y devuelva la cantidad de elementos que estan detras
de este elemento. Si el elemento E no esta en la cola se debe levantar una exception . Se puede asumir que no hay
 valores repetidos . En cualquieras de estos casos se debe mantener el estado original de la cola al finalizar la ejecucion)
 Por ejemplo para la cola  frente |< 4, 6, 2, 3, 1, 7|< ultimo y los siguientes E:
    *) E= 3 hay dos elementos detras, debe devolver 2
    *) E= 7 hay cero elementos detras, debe devolver 0
    *) E= 8 debe levantar una exception
"""
from cola import Cola
def elementos_detras(cola, e):
    cola_aux = Cola()
    contador = 0
    while not cola.esta_vacia():
        dato = cola.desencolar()
        cola_aux.encolar(dato)
        if dato == e:
            break
    while not cola.esta_vacia():
        dato = cola.desencolar()
        cola_aux.encolar(dato)
        contador += 1
    while not cola_aux.esta_vacia():
        cola.encolar(cola_aux.desencolar())
    return contador



cola = Cola()
cola.encolar(4)
cola.encolar(6)
cola.encolar(2)
cola.encolar(3)
cola.encolar(1)
cola.encolar(7)
print(cola)
print(elementos_detras(cola, 3))


