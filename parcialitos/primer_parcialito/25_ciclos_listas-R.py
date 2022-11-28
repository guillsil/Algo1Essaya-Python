"""Implementar una función que reciba una matriz (representada por una lista de listas) y devuelva una nueva matriz
que sea la traspuesta de la original.
"""
def traspuesta(matriz):
    traspuesta = []
    for i in range(len(matriz[0])):# matriz[0] es la dimencion de la columna
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        traspuesta.append(fila)
    return traspuesta
print(traspuesta([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[0])