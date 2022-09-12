"""Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.
b) Devuelva una lista con aquellos que son múltiplos de k."""
# a)
def menores_mayores_iguales(lista, k):
    menores = []
    mayores = []
    iguales = []
    for i in lista:
        if i < k:
            menores.append(i)
        elif i > k:
            mayores.append(i)
        else:
            iguales.append(i)
    return menores, mayores, iguales
assert menores_mayores_iguales([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == ([1, 2, 3, 4], [6, 7, 8, 9, 10], [5])
# b)
def multiplos(lista, k):
    new_lista = []
    for i in lista:
        if i % k == 0:
            new_lista.append(i)
    return new_lista
assert multiplos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [5, 10]