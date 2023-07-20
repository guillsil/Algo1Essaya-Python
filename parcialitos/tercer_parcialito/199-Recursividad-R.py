"""Realizar una función recursiva que reciba una lista de Python de números y devuelva una nueva lista
eliminando los dígitos que son sucedidos por un número primo, devolviendo una lista igual a la recibida por parámetro
pero sin los dígitos que cumplan la condición especificada. Nota: la función es_primo() ya se encuentra implementada.

Ejemplo: eliminar_sucedidos_primo([4,7,6,11,13]) → [7,13]
"""
def es_primo(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def eliminar_sucedidos_por_primos(lista):
    if len(lista) == 1:
        return lista
    else:
        if es_primo(lista[1]):
            return eliminar_sucedidos_por_primos(lista[1:])
        else:
            return [lista[0]] + eliminar_sucedidos_por_primos(lista[1:])

print(eliminar_sucedidos_por_primos([4,7,6,11,13]))