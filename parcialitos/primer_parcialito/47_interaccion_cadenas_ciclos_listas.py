"""Escribir una función que pida cadenas al usuario hasta que ingrese una cadena vacía. Debe devolver una
lista de las palabras ingresadas. Por ejemplo:
Cadena: hola co
Cadena: mo e
Cadena: stas ?
Cadena:
Debe devolver: ['hola', 'como', 'estas', '?']"""
def pedir_cadenas():
    """Pide cadenas al usuario hasta que ingrese una cadena vacía"""
    lista = []
    cadena = input("Cadena: ")
    while cadena != "":
        lista.append(cadena)
        cadena = input("Cadena: ")
    return lista
print(pedir_cadenas())