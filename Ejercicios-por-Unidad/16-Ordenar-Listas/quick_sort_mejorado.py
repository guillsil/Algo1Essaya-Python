def quick_sort(lista):
    """Ordena la lista de forma recursiva .
    Pre: los elelemtos de la lista deben ser comparables
    Post: una nueva lista con los elelemetos ordenados"""
    _quick_sort(lista, 0, len(lista) - 1)

def _quick_sort(lista, inicio, fin):
    """Funcion quick_sort recursiva
    Pre:los indices inicio y fin indican sobre que porción operar
    Post: la lista queda ordenada"""
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)

def _partition(lista, inicio, fin):
    """Funcion Particion que trabaja sobre la misma lista
    Pre: los indices inicio y fin indican sobre que porción operar
    Post: los menores estan antes que el pivote , los mayores despues.
    Devuelve la posicion del pivote"""

    pivote = lista[inicio]
    menores = inicio
    #Ubicar menores a la izquierda , mayores a la derecha
    for i in range(inicio + 1, fin + 1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                _swap(lista, i, menores)
    #ubicar el pivote al final de los menores
    if inicio != menores:
        _swap(lista, inicio, menores)
    return menores

def _swap(lista, i, j):
    """Intercambia los elementos de la lista en las posiciones i y j
    Pre: i y j deben ser indices validos de la lista
    Post: los elementos en las posiciones i y j se intercambian"""
    lista[j], lista[i] =  lista[i], lista[j]