"""Escribir una función que dada una matriz representada como una lista de listgas de números
(donde cada sublista representa una fila), devuelva una lista con los máximos de cada columna. Ejemplo:
maximos_columnas([[1, 2, 8, 4],
                  [6, 7, 3, 3],   →   [6, 7, 8, 9]
                  [6, 5, 4, 9]])"""
#a)
def maximos_columnas(matriz):
    maximos = []
    for i in range(len(matriz[0])):
        maximo = matriz[0][i]
        for j in range(len(matriz)):
            if matriz[j][i] > maximo:
                maximo = matriz[j][i]
        maximos.append(maximo)
    return maximos
print(maximos_columnas([[1, 2, 8, 4],[6, 7, 3, 3],[6, 5, 4, 9]]))