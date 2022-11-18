"""Escribir una función recursiva que reciba 2 enteros n y b y devuelva True si n es
potencia de b.
Ejemplos:
es_potencia(8, 2) -> True
es_potencia(64, 4) -> True
es_potencia(70, 10) -> False"""
def es_potencia(n, b):
    if n == 1:
        return True
    elif n % b != 0:
        return False
    else:
        return es_potencia(n // b, b)
print(es_potencia(8, 2))
print(es_potencia(64, 4))
