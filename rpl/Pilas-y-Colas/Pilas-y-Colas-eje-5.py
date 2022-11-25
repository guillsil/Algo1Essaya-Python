"""Escribir una función llamada tail que recibe un archivo y un número N e imprime
las últimas N líneas del archivo. Durante el transcurso de la función no puede haber más de N
líneas en memoria."""
# #importar la clase pila

from pila import Pila
def tail(archivo, n):
    pila = Pila()
    for linea in archivo:
        pila.apilar(linea)
    for i in range(n):
        print(pila.desapilar())
#prueba
archivo = open('archivo.txt')
tail(archivo, 3)