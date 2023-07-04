"""Implementar el algoritmo de búsqueda binaria de manera recursiva"""
def busqueda_binaria(lista, elemento):
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
lista = [1, 2, 3, 4, 5, 6, 7]
print(busqueda_binaria(lista, 3))
lista = [1, 2, 3, 4, 5, 6, 7]
"""
def busqueda_binaria2(lista, elemento):
    izquierda = 0
    derecha = len(lista) -1 
    medio = (izquierda + derecha) // 2
    if lista[medio] == elemento:
        return medio
    if lista[medio] < elemento:
        return busqueda_binaria2(lista[medio + 1:], elemento)
    else:
        return busqueda_binaria2(lista[:medio], elemento) + izquierda
print(busqueda_binaria2(lista, 3))"""
def busqueda_binaria_recursiva(lista, elemento, izquierda, derecha):
    if izquierda > derecha:
        return -1

    medio = (izquierda + derecha) // 2

    if lista[medio] == elemento:
        return medio
    elif lista[medio] < elemento:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, elemento, izquierda, medio - 1)

# Ejemplo de uso
lista = [1, 2, 3, 4, 5, 6, 7]
elemento = 3
resultado = busqueda_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

if resultado != -1:
    print(f"Elemento encontrado en el índice {resultado}")
else:
    print("Elemento no encontrado en la lista")

