"""Escribir una función que reciba una cadena que contiene únicamente palabras separadas por espacios, y que devuelva 
una nueva cadena con las letras de cada una de las palabras invertidas.
Ejemplo: "Qué día tan bonito" → "éuQ aíd nat otinob"""
def invertir_palabras(cadena):
    """Devuelve una cadena con las letras de cada una de las palabras invertidas."""
    lista = cadena.split()
    cadena_invertida = ""
    for palabra in lista:
        cadena_invertida += palabra[::-1] + " "
    return cadena_invertida
print(invertir_palabras("Qué día tan bonito"))