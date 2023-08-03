"""Escribir una función diferencia_listas que reciba dos listas donde cada una no presenta elementos repetidos y
devuelva la diferencia de la primera con la segunda, entendiendo por diferencia todos los elementos de la primera
que no están en la segunda.
>> diferencia_listas([2,3,1,5], [2,5])
[3,1]
>> diferencia_listas([15,49], [6,31])
[15,49]"""

def diferencia_listas(lista1, lista2):
    """Devuelve la diferencia de la primera lista con la segunda."""
    diferencia = []
    for elemento in lista1:
        if elemento not in lista2:
            diferencia.append(elemento)
    return diferencia
print(diferencia_listas([2,3,1,5], [2,5]))