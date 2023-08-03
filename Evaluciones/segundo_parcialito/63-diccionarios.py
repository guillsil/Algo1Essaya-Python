"""Se propone implementar un sistema de criptografía sencillo en dónde cada carácter del texto a codificar
sea reemplazado por otro. Por ejemplo, un esquema posible sería transformar todas las letras "a" en "b",
todas las "b" en "c", etc. Implementar una función que dada una cadena y un diccionario que represente la
tabla de transformación, devuelva la cadena codificada. Por ejemplo: si la cadena es 'Hola' y el diccionario
contiene {'H': 'e', 'o': 'b', 'l':'m'}, debe devolver 'ebma'."""
def criptografia(cadena, dic):
    cadena_cript = ''
    for c in cadena:
        if c in dic:
            cadena_cript += dic[c]
        else:
            cadena_cript += c
    return cadena_cript

dic = {'H': 'e', 'o': 'b', 'l':'m'}
print(criptografia('Hola', dic))