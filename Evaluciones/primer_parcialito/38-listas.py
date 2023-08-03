"""Escribir una función que reciba una matriz cuadrada (lista de listas), cuyos elementos son números, y que devuelva
la cantidad de elementos en el triángulo superior de la matriz que sean negativos.
Nota: el triángulo superior de una matriz abarca la diagonal principal, y todo lo que esté por arriba de ella.
Ejemplo: si la función recibe la matriz:
[
    [0, 1, -3],
    [0, -4, 5],
    [-9, 8, 1],
]
Entonces debe devolver 2, pues en el triángulo superior solo están los números negativos -3 y -4."""
def cantidad_negativos(matriz):
    """Devuelve la cantidad de elementos negativos en el triángulo superior de la matriz."""
    cantidad = 0
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] < 0:
                cantidad += 1
    return cantidad
print(cantidad_negativos([[0, 1, -3], [0, -4, -5], [-9, 8, -1]]))
