"""Escribir una función que reciba por parámetro dos pilas y modifique su contenido de manera que los elementos de la primer pila queden en la segunda, y los de la segunda en la primera manteniendo el orden original de los elementos. Como estructuras auxiliares, se pueden utilizar únicamente pilas y/o colas."""
from pila import Pila
from cola import Cola

def intercambiarPilas(pila1, pila2):
    # Creamos una pila auxiliar para preservar el orden original de pila2
    pila_aux = Pila()

    # Vaciamos pila1 en pila_aux preservando el orden original
    while not pila1.esta_vacia():
        pila_aux.apilar(pila1.desapilar())

    # Vaciamos pila2 en pila1 preservando el orden original
    while not pila2.esta_vacia():
        pila1.apilar(pila2.desapilar())

    # Vaciamos pila_aux en pila2 preservando el orden original
    while not pila_aux.esta_vacia():
        pila2.apilar(pila_aux.desapilar())

    # Invertimos el orden de pila1 utilizando una cola auxiliar
    cola_aux = Cola()
    while not pila1.esta_vacia():
        cola_aux.encolar(pila1.desapilar())
    
    while not cola_aux.esta_vacia():
        pila1.apilar(cola_aux.desencolar())

    

pila1 = Pila()
pila2 = Pila()
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)
cola1 = Cola()
cola1.encolar(1)
cola1.encolar(2)
cola1.encolar(3)
cola1.desencolar()
cola1.desencolar()

pila2.apilar(4)
pila2.apilar(5)
pila2.apilar(6)

print(pila1)
print(pila2)

intercambiarPilas(pila1, pila2)
print(pila1)
print(pila2)

