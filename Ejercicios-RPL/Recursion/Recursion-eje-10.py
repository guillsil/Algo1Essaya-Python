"""Escribir una función recursiva que dada una cadena determine si en la misma hay más letras
A que letras E.
Ejemplos:
tiene_mas_letra_a('hola') -> True
tiene_mas_letra_a('ayer') -> False
tiene_mas_letra_a('jueves') -> False"""

def tiene_mas_letra_a(cadena):
    '''
    Devuelve True si en la cadena hay más letras A que letras E, False en caso contrario.
    '''
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == 'a' or cadena[0] == 'A':
            return 1 + tiene_mas_letra_a(cadena[1:])
        elif cadena[0] == 'e' or cadena[0] == 'E':
            return -1 + tiene_mas_letra_a(cadena[1:])
        else:
            return tiene_mas_letra_a(cadena[1:])

print(tiene_mas_letra_a('jueves'))
print(tiene_mas_letra_a('ayer'))
print(tiene_mas_letra_a('hola'))
