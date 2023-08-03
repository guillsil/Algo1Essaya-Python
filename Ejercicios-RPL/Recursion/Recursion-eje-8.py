"""Escribir una funcion recursiva que encuentre el mayor elemento de una lista."""
def mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], mayor(lista[1:]))
print(mayor([1, 2, 30, 4, 10000, 6, 7, 8, 9, 10]))