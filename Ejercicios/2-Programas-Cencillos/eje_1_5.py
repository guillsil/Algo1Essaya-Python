"""Escribir una función que, dado un número entero 𝑛, permita calcular su factorial."""

def factorial(numero):
    resultado=1
    for i in range(1, numero+1):
        resultado=resultado*i
    return resultado

#que es un factorial?
#es el producto de todos los numeros enteros positivos desde 1 hasta n
#ejemplo: 5! = 1*2*3*4*5 = 120
#ejemplo: 1! = 1
#ejemplo: 0! = 1
#ejemplo: 2! = 1*2 = 2
#ejemplo: 3! = 1*2*3 = 6
#ejemplo: 4! = 1*2*3*4 = 24
#ejemplo 6! = 1*2*3*4*5*6 = 720

