"""Escribir una función recursiva para replicar los elementos de una lista una can-
tidad n de veces. Por ejemplo:
replicar([1, 3, 3, 7], 2) -> ([1, 1, 3, 3, 3, 3, 7, 7])
"""
def replicar(lista, n):
    if len(lista) == 1:
        return lista * n
    else:
        return lista[:1] * n + replicar(lista[1:], n)
print(replicar([1, 3, 3, 7], 2))