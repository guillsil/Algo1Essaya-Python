"""Escribir una función que, dado un número entero 𝑛, permita calcular su factorial."""

def factorial(numero):
    resultado=1
    for i in range(2, numero+1):
        resultado=resultado*i
    return resultado

print(factorial(7))