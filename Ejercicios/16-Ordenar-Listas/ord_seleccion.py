#ordenar lista por seleccion

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en el segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
    Pre: los elementos de la lista deben ser comparables.
     Post: la lista está ordenada."""
    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        #posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n -= 1

print(ord_seleccion([3,0,4,2,5,7,4,1]))


