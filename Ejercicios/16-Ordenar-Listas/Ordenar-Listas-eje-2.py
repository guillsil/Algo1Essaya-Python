"""Escribir una función merge_sort_3 que funcione igual que el merge sort pero
en lugar de dividir los valores en dos partes iguales, los divida en tres (asumir que se cuenta
con la función merge(lista_1, lista_2, lista_3)). ¿Cómo te parece que se va a comportar
este método con respecto al merge sort original?"""
def  merge_sort(lista):
    """Ordena la lista mediante el metodo mergesort, pero dividiendo en 3 las listas
    Pre: lista debe contener elementos iterables
    Post: la lista queda ordenada"""
    if len(lista) < 2:
        return lista
    tercio = len(lista) // 3
    izquierda = merge_sort(lista[:tercio])
    centro = merge_sort(lista[tercio:tercio*2])
    derecha = merge_sort(lista[tercio*2:])
    return merge(izquierda, centro, derecha)

def merge(lista1, lista2, lista3):
    """Intercala los elementos de lista 1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Post: Devuelve una lista con los elementos de lista1 , lista2 y lista3
    intercalados de forma ordenada."""
    i, j, k = 0, 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2) and k < len(lista3):
        if lista1[i] < lista2[j] and lista1[i] < lista3[k]:
            resultado.append(lista1[i])
            i += 1
        elif lista2[j] < lista1[i] and lista2[j] < lista3[k]:
            resultado.append(lista2[j])
            j += 1
        else:
            resultado.append(lista3[k])
            k += 1

    # Agregar los elementos restantes
    resultado += lista1[i:]
    resultado += lista2[j:]
    resultado += lista3[k:]

    return resultado

print(merge_sort([4, 5, 7, 1, 2, 4, -2, 5, 3]))

#no se si es la mejor forma de hacerlo, pero funciona
