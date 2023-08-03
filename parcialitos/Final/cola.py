class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero is None

    def encolar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return dato

    def __str__(self):
        s = ""
        nodo = self.primero
        while nodo is not None:
            s += str(nodo.dato) + " "
            nodo = nodo.siguiente
        return s

# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
print(cola)

print(cola.desencolar())  # Salida: 1
print(cola.desencolar())  # Salida: 2
print(cola.esta_vacia())  # Salida: False
print(cola.desencolar())  # Salida: 3
print(cola.esta_vacia())  # Salida: True
print(cola)

