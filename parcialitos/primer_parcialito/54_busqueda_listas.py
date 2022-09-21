"""¿Se puede modificar la búsqueda binaria vista en clase para que funcione tanto para listas ordenadas de forma
creciente como para listas en orden decreciente? Si es posible, explicar cómo lo haría y qué problemas o casos
de borde podría encontrar. De lo contrario, explicar claramente por qué no se puede.
Nota: En ningún caso se puede modificar la lista, ni realizar algún cambio que empeore la eficiencia del algoritmo.
"""
def busqueda_binaria_creciente(lista, elemento):
    """Busca un elemento en una lista ordenada de forma creciente"""
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
print(busqueda_binaria_creciente([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

def busqueda_binaria_decreciente(lista, elemento):
    """Busca un elemento en una lista ordenada de forma decreciente"""
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] > elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
print(busqueda_binaria_decreciente([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5))
