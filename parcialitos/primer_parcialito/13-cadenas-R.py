"""Escribir una función que reciba un número complejo representado como una tupla de la forma (parte_real, parte_imaginaria)
y devuelva su representación binómica en una cadena.
Ejemplo:
>> representacion_binomica((3, 6))
“3+6i”
>> representacion_binomica((5, 0))
“5”
>> representacion_binomica((1, -2))
“1-2i”
>> representacion_binomica((0, -4))
“-4i”
"""
def representacion_binomica(complejo):
    representacion_binomica = ""
    if complejo[0] != 0:
        representacion_binomica += str(complejo[0])
    if complejo[1] != 0:
        if complejo[1] > 0:
            if complejo[0] != 0:
                representacion_binomica += "+"
            representacion_binomica += str(complejo[1]) + "i"
        else:
            representacion_binomica += str(complejo[1]) + "i"
    return representacion_binomica
print(representacion_binomica((10, -10)))