"""Implementar el siguiente algoritmo para convertir un entero positivo n de base 10 a binario.

a. Crear una pila. b. Obtener el resto de la división entre el número n y 2 y apilarlo. c. Dividir a n por 2 d. Volver al paso $b$ y continuar mientras que el valor de n sea mayor a 0. e. Imprimir el contenido de la pila.
"""
from pila import Pila

def convertir_a_binario(n):
    pila = Pila()
    while n > 0:
        resto = n % 2
        pila.apilar(resto)
        n //= 2
    while not pila.esta_vacia():
        print(pila.desapilar(), end="")
    

convertir_a_binario(10)