"""Escribir una función que reciba una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.
(No utilizar lista.sort().)"""
def busqueda_binaria(lista, elemento):
    """buqueda binaria:
    Pre:la lista debe estar ordenada
    Post:devuelve -1 si el element no esta en la lista, en caso contrario devuelve la posicion del elemento"""
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
def agregar_elemento(lista, elemento):
    """agrega un elemento a la lista y la ordena"""
    lista.append(elemento)
    lista.sort()
    return lista.index(elemento)
def buscar(lista, elemento):
    if elemento in lista:
        return busqueda_binaria(lista, elemento)
    else:
        agregar_elemento(lista, elemento)
print(buscar([1, 2, 4, 4, 5, 6, 7, 8, 9, 10], 3))