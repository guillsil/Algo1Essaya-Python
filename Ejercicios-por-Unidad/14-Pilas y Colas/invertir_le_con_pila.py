#Este es un ejercicio parecido al 14.5:
from pila import Pila
pila = Pila()
for i in range(0, 4):
	pila.apilar(i)

while not pila.esta_vacia():
	print(pila.desapilar())  # va a mostrar 3, 2, 1, 0

#Se puede aprovechar esto para replantear el ejercicio 13.6, que pide escribir un método para invertir una lista enlazada.

class ListaEnlazada:
    def invertir(self):
        pila = Pila()
        act = self.prim
        while act:
            pila.apilar(act.dato)
            act = act.prox

        act = self.prim
        while act:
            act.dato = pila.desapilar()
            act = act.prox



"""
    ¿Cómo se compara esta solución con la que no usa estructuras auxiliares?
La principal diferencia es el espacio en memoria requerido para la ejecución. La nueva solución termina creando una pila con 
la misma cantidad de elementos que la lista enlazada original, requiriendo el doble de memoria. Si la memoria no es un problema, 
se puede utilizar esta versión sin problemas. """