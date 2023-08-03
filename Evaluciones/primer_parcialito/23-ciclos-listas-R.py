"""Escribir una función que recibe dos secuencias A y B de igual longitud, y devuelve una lista donde el elemento
en la posición i es una tupla con los elementos de A y B en la posición i.
Ejemplo: f([1, 2, 3], [4, 5, 6]) → [(1, 4), (2, 5), (3, 6)]"""

def f(A, B):
    """Devuelve una lista donde el elemento en la posición i es una tupla con los elementos de A y B en la posición i."""
    lista = []
    for i in range(len(A)):
        lista.append((A[i], B[i]))
    return lista
print(f([1, 2, 3], [4, 5, 6]))