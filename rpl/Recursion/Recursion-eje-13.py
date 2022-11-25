"""Implementar el método recursivo invertir de ListaEnlazada, que invierta el orden de la lista
(es decir, el primer elemento queda como último y viceversa). El método no debe recorrer la lista
más de N veces (siendo N la cantidad de elementos de la lista).
Nota: Solo completar el método invertir. El resto de los métodos no deben ser modificados."""
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def __str__(self):
        act = self.prim
        s = ''
        while act:
            s += str(act.dato) + ' '
            act = act.prox
        return s

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def __len__(self):
        return self.cant

    def invertir(self):
        '''
        Invierte el orden de la lista (es decir, el primer elemento queda como último y viceversa).
        El método no debe recorrer la lista más de N veces (siendo N la cantidad de elementos de la lista).
        '''
        def invertir_aux(prim, ant):
            if not prim:
                return ant
            else:
                act = prim.prox
                prim.prox = ant
                return invertir_aux(act, prim)
        self.prim = invertir_aux(self.prim, None)
        return self




#probar
lista = ListaEnlazada()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
print(lista)

print(lista.invertir())