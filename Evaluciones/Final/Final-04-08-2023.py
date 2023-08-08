"""
1)
Dada la clase Cola con los métodos __init__, esta vacía, encolar y desencolar , implementar
la clase ColaConCapacidadMaxima , que tenga los mismos métodos de COla y , además
°)En el constructor debe recibir la capacidad maxíma de la cola
°)Al encolar debe lanzar una exception si no hay capacidad disponible
°)Debe tener un método esta_llena que indica si la cola está llena o no, en tiempo constante
"""
from cola import Cola
class ColaConCapacidadMaxima(Cola):
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cantidad = 0
        self.cola = Cola()

    def encolar(self, dato):
        if self.cantidad == self.capacidad:
            raise ValueError("La cola esta llena")
        self.cola.encolar(dato)
        self.cantidad += 1

    def desencolar(self):
        self.cantidad -= 1
        return self.cola.desencolar()

    def esta_vacia(self):
        return self.cola.esta_vacia()

    def esta_llena(self):
        return self.cantidad == self.capacidad


cola = ColaConCapacidadMaxima(3)
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola.esta_llena())

"""
2)
Implementar la funcion permutaciones(s) que dada una cadena de caracteres imprime todas las permutaciones posibles de la misma.
Ejemplo:
>>> permutaciones("abc")
abc acb
bac bca
cab cba
"""
#iterativa
def permutaciones(cadena):
    for i in range(len(cadena)):
        c = cadena[0]
        cadena = c + cadena[1:]
        print(cadena)
        cadena = cadena[1:] + c


def voltear(cadena):
    return cadena[::-1]

def permutar(cadena):
    otra = voltear(cadena)
    permutaciones(cadena)
    permutaciones(otra)

permutar("abcd")

"""
Escribir una funcion que reciba una matriz (reprersentada conmo listas de listas) , y devuelve una copia de la matriz rotada 180 grados.
Ejemplo:
>>> M = [[1, 2, 3],
         [4, 5, 6],
         ]
>>> rotar_180(M)
[[6, 5, 4],
[3, 2, 1]]
"""
def rotar_fila(fila):
    fila_aux = []
    k = len(fila) -1
    for i in range(len(fila)):
        fila_aux.append(fila[k])
        k -= 1
    return fila_aux

def rotar_180(matriz):
    matriz_nueva = []
    matriz = rotar_fila(matriz)
    for fila in matriz:
        matriz_nueva.append(rotar_fila(fila))
    return matriz_nueva

print(rotar_180([[1, 2, 3], [4, 5, 6]]))

"""
Dada la clase ListaEnlazada implementada únicamente con una referencia al primer nodo , implementar el método reducir, 
que recibe una función f que recibe dos valores y devuelve un nuevo valor . Para los dos primeros nodos de la lista, 
el método debe invocar a f pasándole los datos de ambos nodos , y reemplazar ambos ambos nodos con unico nodo que contiene 
el resultado.
EL método debe aplicar esta operación reiteradas veces hasta que quede un único elemento en la lista. 
Ejemplo:
>>> lista = ListaEnlazada()
>>> lista.insertar(1)
>>> lista.insertar(2)
>>> lista.insertar(3)
>>> lista.insertar(4)
>>> lista.insertar(5)
>>> lista.reducir(lambda x, y: x + y)
>>> lista
[15]d
"""
class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class ListaEnlazada:
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

    def aplicar_f(self, f):
        """
        Aplica la funcion f a los dos primeros nodos de la lista hasta que el ultimo sea NOne
        :param f:
        :return:
        """
        if self.prim is None:
            raise ValueError("Lista vacia")
        actual = self.prim
        while actual is not None and actual.prox is not None:
            dato = f(actual.dato, actual.prox.dato)
            actual.dato = dato
            actual.prox = actual.prox.prox

        return self

lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)
lista.agregar(5)
lista.agregar(6)
print(lista)
lista.aplicar_f(lambda x, y: x + y)
print(lista)

"""
5)
Se tiene un archivo CSV con el formato ciudad, lat, long donde lat y long son números decimales representando la latitud y longitud de la ciudad.
Implementar una funcion que reciba la ruta del archivo CSV y cuatros valores lat1, long2, lat2, long2 representando las dos esquinas opuestas 
de una región rectangular (asumir que lat2 > lat1 y que long2 > long1) y devuelva una lista con las ciudades que se encuentran dentro de la región. 
"""