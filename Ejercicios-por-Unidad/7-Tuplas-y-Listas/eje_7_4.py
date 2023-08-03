"""Vectores
a) Escribir una función que reciba dos vectores y devuelva su producto escalar.
b) Escribir una función que reciba dos vectores y devuelva si son o no ortogonales.
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.
d) Escribir una función que reciba un vector y devuelva su norma."""
# a)
def producto_escalar(v1, v2):
    return sum([i*j for i, j in zip(v1, v2)])
    #sum es una función que suma todos los elementos de una lista
    #zip es una función que une dos listas en una lista de tuplas
print(producto_escalar((1, 2, 3), (4, 5, 6)))
# b)
def ortogonal(v1, v2):
    return producto_escalar(v1, v2) == 0
print(ortogonal((1, 1, 1), (1, -2, 1)))
# c)
def paralelo(v1, v2):
    return producto_escalar(v1, v2) != 0
print(paralelo((1, 1, 1), (2, 2, 2)))
# d)
def norma(v):
    return producto_escalar(v, v)**0.5
print(norma((1, 1, 1)))


