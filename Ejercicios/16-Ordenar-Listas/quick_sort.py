def quick_sort(lista):
    """Ordena la lista de forma recursiva .
    Pre: los elelemtos de la lista deben ser comparables
    Post: una nueva lista con los elelemetos ordenados"""
    if len(lista) < 2:
        return lista
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + [medio] + quick_sort(mayores)

def _partition(lista):
    """Particiona la lista en 3 segmentos: menores, medio y mayores.
    Pre: la lista debe tener al menos un elemento.
    Post: Devuelve  tres listas: menores, medio y mayores."""
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores   