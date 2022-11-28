"""Escribir una función que reciba una cadena y devuelva el resultado de reemplazar todas las apariciones de la
primera letra (ignorando mayúsculas o minúsculas) con un asterisco.
Nota: no se puede usar la funcion str.replace() de Python.
"""
def reemplazar_primera_letra(cadena):
    """Reemplaza la primera letra de la cadena por un asterisco.
    Nota: No usar str.replace() de Python."""
    nueva_cadena = ""
    primera_letra = cadena[0].lower()
    for letra in cadena:
        if letra.lower() == primera_letra:
            nueva_cadena += "*"
        else:
            nueva_cadena += letra
    return nueva_cadena
print(reemplazar_primera_letra("OHola Mundooo"))
