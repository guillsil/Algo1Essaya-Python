"""a. Dadas dos listas ordenadas de números, implementar una función que reciba estas dos listas y
devuelva una nueva lista que tenga los elementos de ambas listas ordenados. El tiempo de ejecución de
 la función debe ser lineal (proporcional a la cantidad total de elementos de las dos listas).
 b. ¿En qué famoso algoritmo de ordenamiento se utiliza el algoritmo del punto anterior?"""
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
def merge(lista1, lista2):
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado
print(merge(lista1, lista2))