"""Realizar una función recursiva que elimine los números pares de una lista de Python que contiene únicamente números."""
#iterativo
def eliminar_pares(lista):
    indice = 0
    while indice < len(lista):  
        if lista[indice] % 2 == 0:
            lista.remove(lista[indice])
        else:
            indice += 1
    return lista
lista = [1,2,3,4,5,6,7,8,9,10]
print(eliminar_pares(lista))

#recursivo
def eliminar_pares2(lista):
    nueva_lista = []
    if len(lista) == 0:
        return lista
    else:
        if lista[0] % 2 == 0:
            return eliminar_pares2(lista[1:])
        else:
            return eliminar_pares2(lista[1:]) + [lista[0]]
        

lista = [1,2,3,4,5,6,7,8,9,10]
print(eliminar_pares2(lista))

    




