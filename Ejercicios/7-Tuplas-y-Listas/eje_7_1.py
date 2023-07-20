"""Escribir una función que reciba una tupla de elementos e indique si se encuentran
ordenados de menor a mayor o no."""
def ordenada(tupla):
    return tupla == tuple(sorted(tupla)) #sorted() ordena una lista
assert ordenada((1, 2, 3, 4, 5)) == True