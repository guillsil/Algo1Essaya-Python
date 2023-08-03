"""Escribir una función que, dada una lista de tuplas de la forma (valor, indice), devuelva una nueva lista generada
con cada valor en su respectivo índice, donde el resto de los índices que no tienen un valor asociado se les asignará
un 0.
Por ejemplo, para la lista de tuplas [(4, 1), (9, 6), (13, 3)] debe devolverse la lista [0, 4, 0, 13, 0, 0, 9].
Nota: El mayor índice de la lista de tuplas corresponde al último índice de la lista final. En el ejemplo el mayor
índice era 6, y el resultado tiene 7 elementos.
Nota 2: Puede asumirse que no hay índices repetidos en las tuplas.
"""
def max_indice(lista):
    """Devuelve el mayor índice de la lista de tuplas."""
    maximo = 0
    for tupla in lista:
        if tupla[1] > maximo:
            maximo = tupla[1]
    return maximo

def lista_tuplas(lista):
    """Devuelve una lista con los valores de la tupla según su índice. Que se encuentra junto a su valor."""
    lista_final = []
    for i in range(max_indice(lista) + 1):
        for tupla in lista:
            if tupla[1] == i:
                lista_final.append(tupla[0])
                break
        else:
            lista_final.append(0)

    return lista_final
print(lista_tuplas([(4, 1), (9, 6), (13, 3), (2, 0), (5, 4), (7, 5), (8, 7), (1, 8)]))