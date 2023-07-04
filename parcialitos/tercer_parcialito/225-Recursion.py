"""Escribir una función recursiva que dadas dos listas de enteros devuelva una nueva lista donde cada i-ésimo elemento representa la suma de los i-ésimos elementos de cada lista. Si no cuentan con la misma cantidad de elementos, la lista resultante deberá tener la misma cantidad de elementos que la menor de las listas. Por ejemplo, para las listas [3, 4, 1, 0, 4] y [0, 2, 7] debe devolverse [3, 6, 8]"""
#iterativo 
def sumar_listas(lista1, lista2):
    nueva_lista = []
    for i in range(min(len(lista1), len(lista2))):
        nueva_lista.append(lista1[i] + lista2[i])
    return nueva_lista

lista1 = [3, 4, 1, 0, 4]
lista2 = [0, 2, 7]
print(sumar_listas(lista1, lista2))
# recursivo
def sumar_listas(lista1, lista2):
    if len(lista1) == 0 or len(lista2) == 0:
        return []
    else:
        return [lista1[0] + lista2[0]] + sumar_listas(lista1[1:], lista2[1:])
lista1 = [3, 4, 1, 0, 4]
lista2 = [0, 2, 7]
print(sumar_listas(lista1, lista2))

