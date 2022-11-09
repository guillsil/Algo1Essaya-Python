"""En la parada del colectivo 130 pueden ocurrir dos eventos diferentes:
• Llega una persona
• Llega un colectivo con 𝑛 asientos libres, y se suben al mismo todas las personas que están
esperando, en orden de llegada, hasta que no quedan asientos libres.
Cada evento se representa con una tupla que incluye:
• El instante de tiempo (cantidad de segundos desde el inicio del día)
• El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
• En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos
libres.
Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuel-
va el promedio de tiempo de espera de los pasajeros en la parada.
Ejemplo:
promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)])
-> 62.6667 (calculado como (45+99+44) / 3)"""
class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None
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

def promedio_espera(eventos):
    cola = Cola()
    suma = 0
    cant = 0
    for evento in eventos:
        if evento[1] == 'p':
            cola.encolar(evento[0])
        else:
            for i in range(evento[2]):
                if not cola.esta_vacia():
                    suma += evento[0] - cola.desencolar()
                    cant += 1
    return suma / cant

print(promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)]))



