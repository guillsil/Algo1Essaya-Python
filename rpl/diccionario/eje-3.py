"""Escribir una función que cuente la cantidad de apariciones de cada
caracter en una cadena de texto, y los devuelva en un diccionario.
Por ejemplo, si se recibe "qué lindo día que hace hoy" debe devolver:

{'q': 2, 'u': 2, 'd': 2, 'o': 2, 'a': 2, 'e': 2, 'h': 2,
'é': 1, 'l': 1, 'i': 1, 'n': 1, 'í': 1, 'c': 1, 'y': 1}"""

def contar_caracteres(cadena):
    diccionario = {}
    # borrar los espacios en blanco
    cadena = cadena.replace(" ", "")
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario
print(contar_caracteres("qué lindo día que hace hoy"))