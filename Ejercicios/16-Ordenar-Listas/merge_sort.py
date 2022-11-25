def  merge_sort(lista):
    """Ordena la lista mediante el metodo mergesort,
    Pre: lista debe contener elemetos iterables
    Post: la lista queda ordenada"""
    if len(lista) < 2:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return merge(izquierda, derecha)

def merge(lista1, lista2):
    """Intercala los elementos de lista 1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Post: Devuelve una lista con los elementos de lista1 y lista2
    intercalados de forma ordenada."""
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar los elementos restantes
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

