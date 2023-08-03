"""Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de
 apariciones de c en s."""

def apariciones(s, c):
    if len(s) == 0:
        return 0
    if s[0] == c:
        return 1 + apariciones(s[1:], c)
    return apariciones(s[1:], c)

print(apariciones("hola, como estas todo tranqui", "a"))