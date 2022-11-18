"""Escribir una funcion recursiva que dada una cadena determine si en la misma
hay más letras A o letras E."""
def mas_a_o_e(cadena):
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == 'a' or cadena[0] == 'A':
            return 1 + mas_a_o_e(cadena[1:])
        elif cadena[0] == 'e' or cadena[0] == 'E':
            return -1 + mas_a_o_e(cadena[1:])
        else:
            return mas_a_o_e(cadena[1:])

print(mas_a_o_e("aeaae"))