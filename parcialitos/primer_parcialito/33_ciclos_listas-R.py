"""Escribir una función que reciba una lista y la invierta sobre la misma lista sin usar estructuras adicionales.
Nota: Al usar slices (lista[::]) se crea una nueva lista, por lo que no se pueden utilizar para resolver este ejercicio"""
def invertir_lista(lista):
    """Invierte la lista sobre sí misma."""
    for i in range(len(lista) // 2):
        lista[i], lista[-i - 1] = lista[-i - 1], lista[i]
    return lista
print(invertir_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
