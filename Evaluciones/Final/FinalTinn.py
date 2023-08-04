"""Resolver los siguientes ejercicios de listas, colas y pilas. (2p)
a. Construir una función
imprimeInverso que imprima los elementos de una lista
enlazada de enteros en orden inverso a partir de una posición
p. (1p)
b. Construir una función que sume los elementos de una lista de enteros recursivamente.
(1p"""
from pila import Pila
from cola import Cola
from lista_enlazada import ListaEnlazada

#a
def imprimir_inverso(lista):
    if lista.esta_vacia():
        raise ValueError("Lista Vacia")
    pila = Pila()
    actual = lista.prim
    while actual is not None:
        pila.apilar(actual.dato)
        actual = actual.prox
    while not pila.esta_vacia():
        print(pila.desapilar())


#b
def suma_recursiva(lista):
    contador = 0
    if lista.esta_vacia():
        return contador
    actual = lista.prim
    contador += actual.dato
    nueva_lista = ListaEnlazada()
    nueva_lista.prim = actual.prox
    return contador + suma_recursiva(nueva_lista)


"""2. Dada una Pila que contiene enteros, escribe una función para ordenarla de forma
ascendente utilizando solo una Pila Auxiliar. No se permite el uso de otras estructuras de
datos. (2p)"""


def ordenar_pila(pila):
    pila_aux = Pila()
    while not pila.esta_vacia():
        dato = pila.desapilar()
        while not pila_aux.esta_vacia() and pila_aux.ver_tope() > dato:
            pila.apilar(pila_aux.desapilar())
        pila_aux.apilar(dato)
    return pila_aux

"""
4. Crea una clase llamada
cuentaBancaria que represente una cuenta bancaria. La clase
debe tener las siguientes características:
 Un constructor que tome como parámetros el nombre del titular de la cuenta y el
saldo inicial.
 Métodos para realizar depósitos y retiros en la cuenta.
 Un método para obtener el saldo actual de la cuenta.
 Un método para imprimir la información de la cuenta (nombre del titular y saldo)
Se deben cumplir todas las condiciones para resolver el ejercicio
"""

class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("No hay saldo suficiente")
        self.saldo -= monto

    def obtener_saldo(self):
        return self.saldo

    def __str__(self):
        print(f"Nombre: {self.nombre} Saldo: {self.saldo}")

