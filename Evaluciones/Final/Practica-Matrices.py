"""Implementar una función suma_matrices(matriz1, matriz2) que reciba dos matrices de igual tamaño
y devuelva una nueva matriz que sea la suma de ambas.
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = suma_matrices(matriz1, matriz2)
# Debe devolver: [[6, 8], [10, 12]]
"""
def sumar_matrices(matriz1, matriz2):
    resultado = []
    fila = []
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
        fila = []
    return resultado
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = sumar_matrices(matriz1, matriz2)
#print(resultado)

"""Implementar una función multiplicar_matrices(matriz1, matriz2) que reciba dos matrices y devuelva
una nueva matriz que sea el resultado de multiplicarlas.
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplicar_matrices(matriz1, matriz2)
# Debe devolver: [[19, 22], [43, 50]]
si es de 3x2 * 2x3 debe delvolver , ejemplo
matriz1 = [[1, 2], [3, 4], [5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
resultado = multiplicar_matrices(matriz1, matriz2)
# Debe devolver: [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
"""

def multiplicar_matrices(matriz1, matriz2):
    resultado = []
    fila = []
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            producto = matriz1[i][0] * matriz2[0][j]
            for k in range(1, len(matriz1[0])):
                producto += matriz1[i][k] * matriz2[k][j]
            fila.append(producto)
            
        resultado.append(fila)
        fila = []
matriz1 = [[1, 2], [3, 4], [5, 6]]
matriz2 = [[7, 8, 9], [10, 11, 12]]
resultado = multiplicar_matrices(matriz1, matriz2)
#print(resultado)

"""
Obtener la diagonal de una matriz: Implementa una función obtener_diagonal(matriz) que reciba una matriz
cuadrada y devuelva una lista con los elementos de su diagonal principal. La diagonal principal es
la línea diagonal que va desde la esquina superior izquierda a la esquina inferior derecha.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = obtener_diagonal(matriz)
# Debe devolver: [1, 5, 9]
"""
def obtener_diagonal(matriz):
    diagonal = []
    k = 0
    for i in range(len(matriz)):
        diagonal.append(matriz[i][k])
        k += 1
    return diagonal

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = obtener_diagonal(matriz)
#print(resultado)

"""Verificar si una matriz es simétrica: Implementa una función es_simetrica(matriz) que reciba una matriz cuadrada y devuelva 
True si es simétrica y False en caso contrario. Una matriz es simétrica si es igual a su matriz transpuesta. 
Ejemplo:
matriz1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
resultado1 = es_simetrica(matriz1)
# Debe devolver: False

matriz2 = [[1, 2, 3], [2, 4, 2], [3, 2, 1]]
resultado2 = es_simetrica(matriz2)
# Debe devolver: True"""
def es_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


matriz1 = [[1, 2, 3], [2, 4, 5], [3, 8, 8]]
resultado1 = es_simetrica(matriz1)
#print(resultado1)
matriz2 = [[1, 2, 3], [2, 4, 2], [3, 2, 1]]
resultado2 = es_simetrica(matriz2)
#print(resultado2)

"""Determinar si una matriz es diagonal: Implementa una función es_diagonal(matriz) que reciba una matriz cuadrada y devuelva True si es una matriz
diagonal y False en caso contrario. Una matriz diagonal es aquella en la que todos los elementos fuera de la diagonal principal son cero.
Ejemplo:
matriz1 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
resultado1 = es_diagonal(matriz1)
# Debe devolver: True

matriz2 = [[1, 0, 0], [0, 2, 1], [0, 0, 3]]
resultado2 = es_diagonal(matriz2)
# Debe devolver: False"""

def es_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i != j and matriz[i][j] != 0:
                return False
    return True


matriz1 = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
resultado1 = es_diagonal(matriz1)
print(resultado1)

matriz2 = [[1, 0, 0], [0, 2, 1], [0, 0, 3]]
resultado2 = es_diagonal(matriz2)
print(resultado2)

"""Obtener la matriz identidad: Implementa una función matriz_identidad(n) que reciba un número entero n y devuelva la matriz
identidad de tamaño n x n. La matriz identidad es una matriz cuadrada en la que todos los elementos de la diagonal
principal son 1 y los demás elementos son 0.
Ejemplo:
resultado = matriz_identidad(3)
# Debe devolver: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]"""
def matriz_identidad(n):
    matriz = []
    fila = []
    for i in range(n):
        for j in range(n):
            if i != j:
                fila.append(0)
            else:
                fila.append(1)
        matriz.append(fila)
        fila = []
    return matriz
resultado = matriz_identidad(3)
print(resultado)

"""Obtener la traza de una matriz: Implementa una función obtener_traza(matriz) que reciba una matriz cuadrada y devuelva
la suma de los elementos de la diagonal principal.
Ejemplo:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = obtener_traza(matriz)
# Debe devolver: 15"""

def obtener_traza(matriz):
    resultado = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                resultado += matriz[i][j]

    return resultado
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = obtener_traza(matriz)
print(resultado)

"""Verificar si una matriz es ortogonal: Implementa una función es_ortogonal(matriz) que reciba una matriz cuadrada y
devuelva True si es una matriz ortogonal y False en caso contrario. Una matriz es ortogonal si su matriz
transpuesta es igual a su inversa.
Ejemplo:
matriz1 = [[1, 0], [0, -1]]
resultado1 = es_ortogonal(matriz1)
# Debe devolver: True

matriz2 = [[1, 1], [1, -1]]
resultado2 = es_ortogonal(matriz2)
# Debe devolver: False"""
def inversa_matriz(matriz):
    matriz_inversa = []
    fila = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            fila.append(matriz[j][i])
        matriz_inversa.append(fila)
        fila = []
    return matriz_inversa

def es_ortogonal(matriz):
    """
    Escribir una funcion que reciba un número entero n , y devuevlava una matriz triangular superior de dimension n x n,
    en forma de lista de listas , cuyos elementos no nulos son los números naturales en orden .
    Por ejemplo: para n = 4 , debe devolver la siguiente matriz:
    [[1, 2, 3, 4],
    [0, 5, 6, 7],
    [0, 0, 8, 9],
    [0, 0, 0, 10]]
    """

    def matriz_singular(n):
        matriz = []
        fila = []
        k = 1
        d = 0
        for i in range(n):
            for j in range(n):
                if j >= d:
                    fila.append(k)
                    k += 1
                else:
                    fila.append(0)
            matriz.append(fila)
            fila = []
            d += 1
        return matriz

    print(matriz_singular(4))





