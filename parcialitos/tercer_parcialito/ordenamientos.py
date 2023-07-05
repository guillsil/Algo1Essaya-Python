#ordnemaiento por seleccion
def buscar_minimo(lista, inicio, fin):
    """Devuelve el índice del mínimo elemento en un segmento de
    lista de Python.
 
    La lista no debe ser vacía.
    inicio y fin son posiciones válidas en la lista, con
    inicio <= fin.
    """
    # Inicializo el mínimo al primer valor del segmento
    pos_min = inicio
    # Recorro el segmento para buscar el mínimo
    for i in range(inicio+1, fin+1):
        if lista[i] < lista[pos_min]:
            pos_min = i
    return pos_min

def seleccion_sort(lista):
    n = len(lista)
    inicio = 0
    while inicio < n-1:
        # Encontrar el elemento mínimo en la sublista no ordenada
        min_idx = buscar_minimo(lista, inicio, n-1)

        #Intercaambiar el elemento mínimo encontrado con el primer elemento de la sublista no ordenada
        lista[inicio], lista[min_idx] = lista[min_idx], lista[inicio]
        inicio += 1
        
# Ejemplo de uso
lista = [64, 25, 12, 22, 11]
seleccion_sort(lista)
print(lista)

#oredenamiento por insercion
def reubicar(lista, posicion):
    valor = lista[posicion]
    while posicion > 0 and lista[posicion - 1] > valor:
        lista[posicion] = lista[posicion - 1]
        posicion -= 1
    lista[posicion] = valor

def ordenamiento_por_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion = i
        reubicar(lista, posicion)

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
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[-1]
        menores = [x for x in lista[:-1] if x <= pivote]
        mayores = [x for x in lista[:-1] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

# Ejemplo de uso
lista = [4, 2, 7, 1, 9, 5]
resultado = quicksort(lista)
print(resultado)