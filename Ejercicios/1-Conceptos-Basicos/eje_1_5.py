"""Escribir una función que, dado un número entero 𝑛, permita calcular su factorial."""

def factorial(n):
    resultado=1
    for i in range(2, n+1):
        resultado=resultado*i
    return resultado

print(factorial(7))