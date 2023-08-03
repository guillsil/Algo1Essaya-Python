"""Implementar el algoritmo de búsqueda binaria de manera recursiva."""
def _busqueda_binaria(lista, elemento, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if lista[medio] == elemento:
        return medio
    if lista[medio] > elemento:
        return _busqueda_binaria(lista, elemento, inicio, medio - 1)
    return _busqueda_binaria(lista, elemento, medio + 1, fin)


def busqueda_binaria(lista, elemento):
    return _busqueda_binaria(lista, elemento, 0, len(lista) - 1)

print(busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 5))
