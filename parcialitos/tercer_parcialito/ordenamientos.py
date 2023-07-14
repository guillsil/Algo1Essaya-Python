#ordnemaiento por seleccion
def seleccion_sort(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

        
# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
seleccion_sort(lista)
print(lista)

#oredenamiento por insercion

def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i
        while posicion > 0 and lista[posicion - 1] > valor_actual:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
        lista[posicion] = valor_actual

# Ejemplo de uso
lista = [5, 2, 4, 6, 1, 3, 10]
ordenamiento_por_insercion(lista)
print(lista)

#ordenamiento merge sort
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
    Pre: lista debe contener elementos comparables.
    Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado

# Ejemplo de uso
lista = [5, 2, 4, 6, 1, 3, 10]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)

#ordenamiento quick sort
def quicksort(lista):
    if len(lista) < 2:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    menores_ordenados = quicksort(menores)
    mayores_ordenados = quicksort(mayores)

    return menores_ordenados + [pivote] + mayores_ordenados

print([2, 3, 4, 7, 1, 2, 5 , 6, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(quicksort([2, 3, 4, 7, 1, 2, 5 , 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]))