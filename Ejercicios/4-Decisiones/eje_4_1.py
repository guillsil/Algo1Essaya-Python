"""Escribir dos funciones que resuelvan los siguientes problemas:
a) Dado un número entero 𝑛, indicar si es par o no.
b) Dado un número entero 𝑛, indicar si es primo o no."""
def es_par(n):
    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

def es_primo(n):
    if n % n == 0 or n % 1 == 0:
        print("El número es primo")
    else:
        print("El número no es primo")

es_par(4)
es_primo(5)