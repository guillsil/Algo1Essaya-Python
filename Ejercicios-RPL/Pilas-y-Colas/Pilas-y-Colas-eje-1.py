"""En la parada del colectivo 130 pueden ocurrir dos eventos diferentes:

    Llega una persona
    Llega un colectivo con n asientos libres, y se suben al mismo todas las personas que están esperando,
    en orden de llegada, hasta que no quedan asientos libres.

Cada evento se representa con una tupla que incluye:

    El instante de tiempo (cantidad de segundos desde el inicio del día)
    El tipo de evento, que puede ser 'p' (persona) o 'c' (colectivo).
    En el caso de un evento de tipo 'c' hay un tercer elemento que es la cantidad de asientos
    libres.

Escribir una función que recibe una lista de eventos, ordenados cronológicamente, y devuelva el promedio de tiempo de
espera de los pasajeros en la parada.
Ejemplo:
promedio_espera([(35,'p'), (43,'p'), (80,'c',1), (98,'p'), (142,'c',2)])
    -> 62.6667 (calculado como (45+99+44) / 3)
Nota: Se encuentran disponibles los TDA Pila y Cola con sus métodos ya definidos en los archivos pila.py y cola.py
respectivamente"""
from pila import Pila
from cola import Cola
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox

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
