"""Explicar los pasos del ordenamiento de la lista [1,2,5,7,6,4,0,3] usando el algoritmo de Quicksort"""

def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivote = lista[0]
        menores = [i for i in lista[1:] if i <= pivote]
        mayores = [i for i in lista[1:] if i > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort([1,2,5,7,6,4,0,3]))

#Implementar el algoritmo de ordenamiento por selección
def seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista
print(seleccion([9, 8, 7, 6, 5, 4, 3, 2, 1]))