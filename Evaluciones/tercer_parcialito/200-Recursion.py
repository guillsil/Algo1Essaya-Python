"""Realizar una función recursiva que elimine los números pares de una lista de Python que contiene únicamente números"""
def eliminar_pares(lista):
    if lista == []:
        return []
    if lista[0] % 2 == 0:
        return eliminar_pares(lista[1:])
    return [lista[0]] + eliminar_pares(lista[1:])

print(eliminar_pares([1,2,3,4,5,6,7,8,9,10]))