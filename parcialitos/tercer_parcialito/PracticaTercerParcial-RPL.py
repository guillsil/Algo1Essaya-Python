"""Escribir un método de ListaEnlazada que permita rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva.
Además, el método no debe recorrer la lista N veces si hay que hacer una rotación de N elementos. Asumir que N siempre es >= 0.

La implementación de LE contiene una referencia al primer nodo (self.prim) y un atributo con la longitud (self.cant).
Cada nodo tiene un atributo para el dato dato y el próximo nodo prox.

Ejemplos: dada la LE [1, 2, 3, 4, 5, 6, 7, 8] (self.cant = 8)

le.rotar(0) -> [1, 2, 3, 4, 5, 6, 7, 8]
le.rotar(2) -> [3, 4, 5, 6, 7, 8, 1, 2]
le.rotar(11) -> [4, 5, 6, 7, 8, 1, 2, 3]
le.rotar(10) -> [3, 4, 5, 6, 7, 8, 1, 2]"""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.cant = 0

    def agregar_elemento(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo
        self.cant += 1

    def __str__(self):
        if self.primero is None:
            return "[]"

        actual = self.primero
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + " ".join(elementos) + "]"
    def rotar(self, n):
        """Rotar la lista en N posiciones. El método debe modificar la lista y no devolver una nueva."""

        if self.primero is None:
            raise Exception("Lista Vacia")
        if n == 0:
            return 
        if n > self.cant:
            n = n % self.cant
        if n == self.cant:
            return
        
        nodo_actual = self.primero
        nodo_anterior = None
        contador = 0
    
        while contador < n:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            contador += 1

        nodo_anterior.siguiente = None
        temporal = nodo_actual

        while nodo_actual.siguiente is not None:
            nodo_actual = nodo_actual.siguiente

        nodo_actual.siguiente = self.primero
        self.primero = temporal

    

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(5)
lista.agregar_elemento(6)
lista.agregar_elemento(7)
lista.agregar_elemento(8)

print(lista)
lista.rotar(2)
print(lista)



"""Implementar un método de la clase ListaEnlazada que elimine sobre la misma lista los elementos consecutivos repetidos. La misma está implementada con únicamente una referencia al primer nodo self.prim y cada nodo tiene los atributos para su dato dato y su próximo nodo prox.

Ejemplo:

L: [3 4 4 4 1 4] -> L.eliminar_consecutivos() -> L: [3 4 1 4]"""
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
    
    def eleiminar_consecutivos(self):
        """Elimina los elementos consecutivos repetidos de la lista"""
        if self.primero is None:
            raise Exception("Lista Vacia")
        nodo_actual = self.primero
        nodo_anterior = Nodo(None)
        while nodo_actual is not None:
            if nodo_anterior.dato == nodo_actual.dato:
                nodo_actual = nodo_actual.siguiente
                nodo_anterior.siguiente = nodo_actual
            else:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
        return self.primero
    
lista = ListaEnlazada()
lista.agregar_elemento(3)
lista.agregar_elemento(4)
lista.agregar_elemento(4)
lista.agregar_elemento(4)
lista.agregar_elemento(1)
lista.agregar_elemento(4)

"""print(lista)
lista.eleiminar_consecutivos()
print(lista)"""

"""Sea la siguiente operación, aplicable a cualquier número entero positivo:

    Si el número es par, se divide por 2.
    Si el número es impar, se multiplica por 3 y se suma 1.

La conjetura de Collatz dice que, para cualquier número con el que comencemos, si aplicamos la operación sucesivamente, siempre alcanzaremos el número 1. Escribir la función recursiva collatz(n) que imprime la secuencia de operaciones comenzando desde el número n, y terminando en el número 1.

Ejemplo:

>>> collatz(5)
5
16
8
4
2
1
"""
#iterativo:
def collatzs(numero):
    
    print(numero)
    while numero != 1:
        if numero % 2==0:
            numero = numero / 2
            print(int(numero))
            
        else:
            numero = numero*3 +1
            print(int(numero))
print(collatzs(5))

#recursiva

def collatzs2(numero):
    """Realiza la conjetura de collatz de manera recursiva"""
    print(numero, end="\n")
    if numero == 1:
        return
    if numero % 2==0:
        collatzs2(int(numero/2))
    else:
        collatzs2(int(numero*3 +1))


print(collatzs2(5))

"""Implementar una función intercalar(colas) que reciba una secuencia de colas y devuelva una cola con los elementos de todas las colas intercalados, manteniendo el orden relativo. Las colas originales deben quedar vacías.

Ejemplo 1:

intercalar([Cola(1, 2), Cola(3, 4, 5, 6), Cola(7)])
 -> 
Cola(1, 3, 7, 2, 4, 5, 6)

Ejemplo 2:

intercalar([Cola(0), Cola(10, 11), Cola(20, 21)])
 ->
Cola(0, 10, 20, 11, 21) """
from cola import Cola

def intercalar(colas):
    cola_intercolada = Cola()
    
    for cola in colas:
        while not cola.esta_vacia():
            cola_intercolada.encolar(cola.desencolar())

    return cola_intercolada

cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)

cola2 = Cola()
cola2.encolar(5)
cola2.encolar(6)
cola2.encolar(7)
cola2.encolar(8)

cola3 = Cola()
cola3.encolar(9)

print(intercalar([cola, cola2, cola3]))

"""Implementar una función intercalar(pilas) que reciba una secuencia de pilas y devuelva una pila con los elementos de todas las pilas intercalados, manteniendo el orden relativo. Las pilas originales deben quedar vacías.
Ejemplo:
intercalar([Pila(1, 2), Pila(3, 4, 5, 6), Pila(7)])
    ->
Pila(7, 3, 1, 6, 4, 2)
"""
from pila import Pila

def intercalar_pilas(pilas):
    pila_intercolada = Pila()

    for pila in pilas:
        while not pila.esta_vacia():
            pila_intercolada.apilar(pila.desapilar())

    return pila_intercolada


pila1= Pila()
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)

pila2= Pila()
pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)

pila3= Pila()
pila3.apilar(7)
pila3.apilar(8)
pila3.apilar(9)

print(intercalar_pilas([pila1, pila2, pila3]))


"""Se encontraron incongruencias en los planes preventivos de la pandemia de COBID20. El plan del país lleva una serie de fases a cumplir las cuales estan insertadas en una cola de menor a mayor. De alguna manera hay fases intercaladas que no estaban en el plan y se nos exige removerlas.

Se pide entonces escribir una función que dada dicha cola de fases, la modifique de forma que sólo quede una serie de fases ordenadas.

Ejemplo 1:

sale <| 1 2 6 3 5 4 5 6 7 |< entra
debería quedar la cola:
sale <| 1 2 6 7 |< entra

Ejemplo 2:

sale <| 1 5 4 3 2 8 |< entra
debería quedar la cola:
sale <| 1 5 8 |< entra"""







        
