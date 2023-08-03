"""Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método
debe modificar la lista y no devolver una nueva.
Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos.
Asumir que N siempre es >= 0.
La implementación de LE contiene una referencia al primer nodo (self.prim) y un atributo con la
longitud (self.cant).
Cada nodo tiene un atributo para el dato dato y el próximo nodo prox.
Ejemplos: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (self.cant = 8)
le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(3) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]"""

from pila import Pila
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        self.prim = None
        self.cant = 0

    def __len__(self):
        return self.cant

    def __iter__(self):
        nodo = self.prim
        while nodo:
            yield nodo.dato
            nodo = nodo.prox

    def invertir(self):
        pila = Pila()

        actual = self.prim
        while actual:
            pila.apilar(actual.dato)
            actual = actual.prox

        actual = self.prim
        while actual:
            actugal.dato = pila.desapilar()
            actual = actual.prox

    def suma_acumulativa(self):
        le = ListaEnlazada()
        suma = 0

        act_self = self.prim
        act_otra = None

        while act_self:
            suma += act_self.dato
            nuevo = _Nodo(suma)
            if act_otra:
                suma = act_otra.dato + act_self.dato
                act_otra.prox = nuevo
            else:
                le.prim = nuevo
            act_otra = nuevo

            act_self = act_self.prox

        return le

    def insertar(self, dato):
        nodo = _Nodo(dato)
        nodo.prox = self.prim
        self.prim = nodo
        self.cant += 1

    def rotar(self, n):
        if n > 0:
            n = n % self.cant
            if n == 0:
                return
            nodo = self.prim
            for i in range(n-1):
                nodo = nodo.prox
            nodo2 = nodo.prox
            nodo.prox = None
            nodo = nodo2
            while nodo.prox:
                nodo = nodo.prox
            nodo.prox = self.prim
            self.prim = nodo2

    def rotar2(self, n):
        if not self.prim or self.prim.prox:
            return
        n = n % self.cant
        if n == 0:
            return
        ant = None
        act = None
        ult = self.prim

        i = 0
        while ult.prox:
            if i == n-1:
                ant = ult
                act = ant.prox
            i -= 1
            ult = ult.prox

        ant.prox = None
        ult.prox = self.prim
        self.prim = act
         

"""Escribir una funcion recursiva en Python que ordene una Pila (La cual contiene unicamente números) de menor a mayor 
(quedando el eleemento mas grande en el tope de la pila).)"""

def ordenar_pila(pila):
    if not pila.esta_vacia():
        aux = pila.desapilar()
        ordenar_pila(pila)
        insertar_en_pila(pila, aux)

def insertar_en_pila(pila, dato):
    if pila.esta_vacia() or dato > pila.ver_tope():
        pila.apilar(dato)
    else:
        aux = pila.desapilar()
        insertar_en_pila(pila, dato)
        pila.apilar(aux)

p = Pila()
p.apilar(4)
p.apilar(2)
p.apilar(5)
p.apilar(1)
p.apilar(3)

ordenar_pila(p)
print(p)