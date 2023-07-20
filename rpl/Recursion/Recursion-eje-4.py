"""Escribir una funcion recursiva que reciba como parámetros dos cadenas a y b, y
devuelva una lista con las posiciones en donde se encuentra b dentro de a.
Ejemplo:
posiciones_de("Un tete a tete con Tete", "te") -> [3, 5, 10, 12, 21]"""


def posiciones_de(a, b):
    '''
    DOC: Completar
    '''
    if len(a) < len(b):
        return []
    elif a[:len(b)] == b:
        return [0] + [x + 2 for x in posiciones_de(a[len(b):], b)]
    else:
        return [x + 1 for x in posiciones_de(a[1:], b)]

#prueba
print(posiciones_de("Un tete a tete con Tete", "te"))