"""Escribir una función traducir_a_ingles, que recibe una cadena a traducir y un diccionario cuyas claves
son palabras en español y el valor asociado a cada una es su traducción al inglés, y devuelva la
traducida. En caso que una palabra de la cadena no se encuentre en el diccionario, la función debe incluir
la palabra sin traducir. Asumir que todas las palabras, tanto de la cadena como las del diccionario, están
en minúscula."""
def traductor(cadena, diccionario):
    """Traduce una cadena de español a inglés"""
    palabras = cadena.split()
    for palabra in palabras:
        if palabra in diccionario:
            palabras[palabras.index(palabra)] = diccionario[palabra]
    return ' '.join(palabras)
diccionario = {"hola": "hello", "mundo": "world"}
print(traductor("hola mundo todo bien", diccionario))
