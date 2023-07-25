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