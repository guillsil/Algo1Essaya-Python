"""Escribir una función empaquetar para una lista, donde epaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
, (1, 2), (3, 2)]."""
def empaquetar(lista):
    new_list = []
    for i in range(len(lista)):
        if i == 0:
            new_list.append((lista[i], 1))
        elif lista[i] == lista[i-1]:
            new_list[-1] = (lista[i], new_list[-1][1]+1)
        else:
            new_list.append((lista[i], 1))
    return new_list
assert empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) == [(1, 3), (3, 1), (5, 1), (1, 2), (3, 2)]
