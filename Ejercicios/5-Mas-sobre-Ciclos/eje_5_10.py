"""Escribir una función que reciba un número natural e imprima todos los números
primos que hay hasta ese número."""
def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    for i in range(2, n+1):
        if es_primo(i):
            print(i)
