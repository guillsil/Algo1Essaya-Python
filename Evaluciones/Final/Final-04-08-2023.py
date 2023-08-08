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

        