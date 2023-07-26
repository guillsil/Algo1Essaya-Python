#Escribir la clase pila con los metodos apilar, desapilar, esta_vacia y ver_tope
#Escribir la clase cola con los metodos encolar, desencolar, esta_vacia y ver_frente

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox


class Pila:
    def __init__(self):
        '''
        Inicializa una nueva pila, vacía
        '''
        self.tope = None

    def apilar(self, dato):
        '''
        Agrega un nuevo elemento a la pila
        '''
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo

    def desapilar(self):
        '''
        Desapila el elemento que está en el tope de la pila
        y lo devuelve.
        Pre: la pila NO está vacía.
        Pos: el nuevo tope es el que estaba abajo del tope anterior
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        '''
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def esta_vacia(self):
        '''
        Devuelve True o False según si la pila está vacía o no
        '''
        return self.tope is None

    def __str__(self):
        '''
        Devuelve una representación en cadena de la pila
        '''
        cadena = ""
        nodo = self.tope
        while nodo is not None:
            cadena += str(nodo.dato) + ""
            nodo = nodo.prox
        return cadena


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

"""Ordenar Pila en Forma Ascendente: Implementar una función ordenar_pila_ascendente(pila) que reciba una pila que
contiene enteros y la ordene en forma ascendente utilizando solo una pila auxiliar. No se permite el uso de otras
estructuras de datos. Se debe mantener el orden relativo de los elementos."""
def ordenar_pila_ascendente(pila):
    pila_aux = Pila()
    while not pila.esta_vacia():
        dato = pila.desapilar()
        while not pila_aux.esta_vacia() and pila_aux.ver_tope() > dato:
            pila.apilar(pila_aux.desapilar())
        pila_aux.apilar(dato)
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
    return pila

"""Encolar en Medio: Implementar una función encolar_en_medio(cola, elemento) que reciba una cola y un elemento, y encole 
el elemento en la mitad de la cola. Si la cola tiene un número par de elementos, el elemento debe ser encolado justo 
en la mitad. Si la cola tiene un número impar de elementos, el elemento debe ser encolado justo después de la mitad.
"""
def encolar_en_medio(cola, elemento):
    cola_aux = Cola()
    len = 0
    while not cola.esta_vacia():
        cola_aux.encolar(cola.desencolar())
        len += 1
    if len % 2 == 0:
        for i in range(len//2):
            cola.encolar(cola_aux.desencolar())
        cola.encolar(elemento)
        for i in range(len//2):
            cola.encolar(cola_aux.desencolar())
    else:
        for i in range(len//2+1):
            cola.encolar(cola_aux.desencolar())
        cola.encolar(elemento)
        for i in range(len//2):
            cola.encolar(cola_aux.desencolar())
    return cola
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)
cola.encolar(6)
cola.encolar(7)
cola.encolar(8)
cola.encolar(9)

print(encolar_en_medio(cola, 3))
print(cola)


"""Rotar Cola: Implementar una función rotar_cola(cola, k) que reciba una cola y un número entero k, y rote la cola k veces
hacia la derecha. Es decir, los últimos k elementos de la cola pasan a ser los primeros. Si k es negativo, la rotación se
realiza hacia la izquierda. No se permite el uso de estructuras auxiliares.
Ejemplo:
cola = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rotar_cola(cola, 3)
cola = [7, 8, 9, 1, 2, 3, 4, 5, 6]
rotar_cola(cola, -2)
cola = [3, 4, 5, 6, 7, 8, 9, 1, 2]"""

def rotar_cola(cola, k):
    if k > 0:
        for i in range(k):
            cola.encolar(cola.desencolar())
    else:
        for i in range(abs(k)):
            cola.encolar(cola.desencolar())
    return cola

print(rotar_cola(cola, 2))

"""Combinar Pilas: Implementa una función combinar_pilas(pila1, pila2) que reciba dos pilas y devuelva una nueva pila que contenga los
elementos de ambas pilas combinados en orden. La primera pila debe ir al tope de la nueva pila."""

def combinar_pilas(pila1, pila2):
    pila3 = Pila()
    while not pila1.esta_vacia():
        pila3.apilar(pila1.desapilar())
    while not pila2.esta_vacia():
        pila3.apilar(pila2.desapilar())
    return pila3

"""Desencolar N Elementos: Implementa una función desencolar_n_elementos(cola, n) que desencole los primeros N elementos de una cola y 
los devuelva como una nueva cola. Si N es mayor que la cantidad de elementos en la cola, debe devolver todos los elementos de 
la cola original."""
def desencolar_n_elementos(cola, n):
    cola_aux = Cola()
    len = 0
    while not cola.esta_vacia():
        cola_aux.encolar(cola.desencolar())
        len += 1
    if n > len:
        return cola_aux

    for i in range(n):
        cola.encolar(cola_aux.desencolar())
    return cola
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
desencolar_n_elementos(cola, 2)
print(cola)

"""Pila con Suma Acumulada: Implementa una clase PilaConSuma que tenga los mismos métodos de una pila tradicional (apilar y desapilar),
pero además tenga un método obtener_suma_acumulada() que devuelva la suma acumulada de todos los elementos en la pila."""
class PilaConSuma:
    def __init__(self):
        self.tope = None
        self.suma = 0

    def esta_vacia(self):
        return self.tope is None

    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo
        self.suma += dato

    def desapilar(self):
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self.tope.dato
        self.suma -= dato
        self.tope = self.tope.prox
        return dato

    def obtener_suma_acumulada(self):
        return self.suma

    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self.tope.dato

    def __str__(self):
        cadena = ""
        nodo = self.tope
        while nodo is not None:
            cadena += str(nodo.dato) + ""
            nodo = nodo.prox
        return cadena

"""Cola Prioritaria: Implementa una clase ColaPrioritaria que permita encolar elementos con una prioridad asociada. 
Los elementos con mayor prioridad deben ser desencolados antes que aquellos con menor prioridad. 
Puedes implementar la clase utilizando dos colas separadas para cada prioridad y alternando entre ellas al encolar."""

class ColaPrioritaria:
    def __init__(self):
        self.cola1 = Cola()
        self.cola2 = Cola()

    def encolar(self, dato, prioridad):
        if prioridad == 1:
            self.cola1.encolar(dato)
        else:
            self.cola2.encolar(dato)

    def desencolar(self):
        if not self.cola1.esta_vacia():
            return self.cola1.desencolar()
        else:
            return self.cola2.desencolar()

    def ver_frente(self):
        if not self.cola1.esta_vacia():
            return self.cola1.ver_frente()
        else:
            return self.cola2.ver_frente()

    def esta_vacia(self):
        return self.cola1.esta_vacia() and self.cola2.esta_vacia()

    def __str__(self):
        return str(self.cola1) + str(self.cola2)

cola = ColaPrioritaria()
cola.encolar(1, 1)
cola.encolar(2, 1)
cola.encolar(3, 1)
cola.encolar(4, 2)
cola.encolar(5, 2)
cola.encolar(6, 2)
print(cola)

"""Cola con Máximo: Implementa una clase ColaConMaximo que tenga los mismos métodos de una cola tradicional
(encolar y desencolar), pero además tenga un método obtener_maximo() que devuelva el
elemento máximo presente en la cola."""

class ColaConMaximo:
    def __init__(self):
        self.cola = Cola()
        self.maximo = None

    def encolar(self, dato):
        self.cola.encolar(dato)
        if self.maximo is None or dato > self.maximo:
            self.maximo = dato

"""Pila Ordenada: Implementa una clase PilaOrdenada que acepte elementos en orden y asegure que siempre se mantenga ordenada 
(por ejemplo, en orden ascendente). Al desapilar elementos, se deben mantener ordenados."""
