"""Escribir una función que reciba un número entero 𝑘 e imprima su descomposición
en factores primos."""
def descomposicion(n):
    i = 2#no incluye el 0 y 1
    while i <= n:
        if n % i == 0:
            print(i)
            n = n / i
        else:
            i += 1
descomposicion(100)