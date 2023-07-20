"""Escribir las clases Impresora y Oficina que permita modelar el funcionamiento
de un conjunto de impresoras conectadas en red.
Una impresora:
• Tiene un nombre, y una capacidad máxima de tinta.
• Permite encolar un documento para imprimir (recibiendo el nombre del documento).
• Permite imprimir el documento que está al frente de la cola.
– Si no hay documentos encolados, se muestra un mensaje informándolo.
– Si no hay tinta suficiente, se muestra un mensaje informándolo.
– En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
• Permite cargar el cartucho de tinta
Una oficina:
• Permite agregar una impresora
• Permite obtener una impresora por nombre
• Permite quitar una impresora por nombre
• Permite obtener la impresora que tenga menos documentos encolados.
Ejemplo:
>> o = Oficina()
>> o.agregar_impresora(Impresora('HP1234', 1))
>> o.agregar_impresora(Impresora('Epson666', 5))
>> o.impresora('HP1234').encolar('tp1.pdf')
>> o.impresora('Epson666').encolar('tp2.pdf')
>> o.impresora('HP1234').encolar('tp3.pdf')
>> o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
>> o.impresora('HP1234').imprimir()
tp1.pdf impreso
>> o.impresora('HP1234').imprimir()
No tengo tinta :(
>> o.impresora('HP1234').cargar_tinta()
>> o.impresora('HP1234').imprimir()
tp3.pdf impreso"""
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def encolar(self, dato):
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.primero = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        dato = self.primero.dato
        self.primero = self.primero.prox
        if self.primero is None:
            self.ultimo = None
        return dato

    def ver_primero(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self.primero.dato

    def esta_vacia(self):
        return self.primero is None

    def tamanio(self):
        cantidad = 0
        nodo = self.primero
        while nodo is not None:
            cantidad += 1
            nodo = nodo.prox
        return cantidad

class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        return self.items[-1]

class Impresora:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.cola = Cola()
        self.tinta = capacidad

    def encolar(self, documento):
        self.cola.encolar(documento)

    def imprimir(self):
        if self.cola.esta_vacia():
            print("No hay documentos encolados")
        elif self.tinta == 0:
            print("No tengo tinta")
        else:
            self.tinta -= 1
            print(self.cola.desencolar(), "impreso")

    def cargar_tinta(self):
        self.tinta = self.capacidad

class Oficina:
    def __init__(self):
        self.impresoras = []

    def agregar_impresora(self, impresora):
        self.impresoras.append(impresora)

    def impresora(self, nombre):
        for impresora in self.impresoras:
            if impresora.nombre == nombre:
                return impresora
        raise ValueError("No existe la impresora")

    def quitar_impresora(self, nombre):
        for impresora in self.impresoras:
            if impresora.nombre == nombre:
                self.impresoras.remove(impresora)
                return
        raise ValueError("No existe la impresora")

    def obtener_impresora_libre(self):
        impresora_libre = None
        for impresora in self.impresoras:
            if impresora_libre is None:
                impresora_libre = impresora
            elif impresora.cola.tamanio() < impresora_libre.cola.tamanio():
                impresora_libre = impresora
        return impresora_libre

o = Oficina()
o.agregar_impresora(Impresora('HP1234', 1))
o.agregar_impresora(Impresora('Epson666', 5))
o.impresora('HP1234').encolar('tp1.pdf')
o.impresora('Epson666').encolar('tp2.pdf')
o.impresora('HP1234').encolar('tp3.pdf')
o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
o.impresora('HP1234').imprimir()
o.impresora('HP1234').imprimir()
o.impresora('HP1234').cargar_tinta()
o.impresora('HP1234').imprimir()