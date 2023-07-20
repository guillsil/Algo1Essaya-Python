"""Implementar la función merge en forma recursiva. La función recibe dos listas ordenadas y devuelve una lista
 con los elementos intercalados ordenadamente."""
def merge(lista1, lista2):
    """Recibe dos listas ordenadas y devuelve una lista con los elementos intercalados ordenadamente."""
    if lista1 == []:
        return lista2
    elif lista2 == []:
        return lista1
    elif lista1[0] < lista2[0]:
        return [lista1[0]] + merge(lista1[1:], lista2)
    else:
        return [lista2[0]] + merge(lista1, lista2[1:])

print(merge([1, 3, 5, 7], [2, 4, 6, 8]))

