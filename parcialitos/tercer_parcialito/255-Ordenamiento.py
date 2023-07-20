"""Implementar el algoritmo de ordenamiento por selección utilizando el mínimo en vez del máximo."""
def ord_seleccion(lista):
    n = len(lista) -1
    while n >0:
        p = buscar_min(lista, 0, n)
        lista[n], lista[p] = lista[p], lista[n]
        n -= 1
    return lista

def buscar_min(lista, inicio, fin):
    p = inicio
    for i in range(inicio + 1, fin + 1):
        if lista[i] > lista[p]:
            p = i
    return p

print(ord_seleccion([5, 3, 8, 1, 2, 9, 4, 7, 6]))