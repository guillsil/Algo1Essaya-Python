"""Dada una pila con números, escribir una función recursiva que calcule el producto de los mismos. La pila
debe quedar en su estado original al final de la ejecución."""
from pila import Pila
def producto(pila):
    if pila.esta_vacia():
        return 1
    else:
        dato = pila.desapilar()
        producto_aux = producto(pila)
        pila.apilar(dato)
        return producto_aux * dato

pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)

print(producto(pila))