"""Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números."""
# a)
def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def primos(lista):
    new_lista = []
    for i in range(2    , len(lista)+1):
        if es_primo(i):
            new_lista.append(i)
    return new_lista
assert primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [2, 3, 5, 7, 11]
# b)
def sumatoria_y_promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma, suma/len(lista)
assert sumatoria_y_promedio([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (55, 5.5)
# c)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
def factoriales(lista):
    new_lista = []
    for i in lista:
        new_lista.append(factorial(i))
    return new_lista
assert factoriales([1, 2, 3, 4, 5]) == [1, 2, 6, 24, 120]



