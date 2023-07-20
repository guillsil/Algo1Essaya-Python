"""Escribir una función que reciba una lista de tuplas de la forma (n, m) y devuelva dos listas. La primera tendrá
los elementos de la primer posicion de las tuplas, y la segunda, los que estén en la segunda posición."""
def separar_tuplas(lista):
    """Devuelve dos listas, una con los elementos de la primer posición de las tuplas, y la otra con los de la segunda."""
    lista1 = []
    lista2 = []
    for tupla in lista:
        lista1.append(tupla[0])
        lista2.append(tupla[1])
    return lista1, lista2

print(separar_tuplas([(1, 2), (3, 4), (5, 6)]))