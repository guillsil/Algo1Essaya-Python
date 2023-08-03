"""Matrices.
a) Escribir una función que reciba dos matrices y devuelva la suma.
b) Escribir una función que reciba dos matrices y devuelva el producto.
c) ⋆ Escribir una función que opere sobre una matriz y mediante eliminación gaussiana de-
vuelva una matriz triangular superior.
d) ⋆ Escribir una función que indique si un grupo de vectores, recibidos mediante una
lista, son linealmente independientes o no."""
# a)
def sumas_de_matrices(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += m2[i][j]
    return m1
"""print(sumas_de_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))"""
# b)
def producto_de_matrices(m1, m2):
    new_matrix = []
    for i in range(len(m1)):
        new_matrix.append([])
        for j in range(len(m1[0])):
            new_matrix[i].append(0)
            for k in range(len(m1[0])):
                new_matrix[i][j] += m1[i][k] * m2[k][j]
    return new_matrix
"""print(producto_de_matrices([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))"""
# c)
def eliminacion_gaussiana(m):
    for i in range(len(m)):
        for j in range(i+1, len(m)):
            if m[j][i] != 0:
                factor = m[j][i] / m[i][i]
                for k in range(i, len(m)):
                    m[j][k] -= factor * m[i][k]
    return m
"""print(eliminacion_gaussiana([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))"""
# d)
def linealmente_independientes(v):
    m = []
    for i in range(len(v)):
        m.append([])
        for j in range(len(v[0])):
            m[i].append(v[i][j])
    return eliminacion_gaussiana(m) == m
print(linealmente_independientes([[1, 0, 0], [0, 1, 0], [0, 0, 0]]))

