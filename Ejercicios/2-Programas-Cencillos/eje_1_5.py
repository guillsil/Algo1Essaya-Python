"""Escribir una función que, dado un número entero 𝑛, permita calcular su factorial."""

def factorial(numero):
    resultado=1
    for i in range(1, numero+1):
        resultado=resultado*i
    return resultado

