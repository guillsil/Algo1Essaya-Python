"""Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra
en la cadena. Por ejemplo, si recibe ”que lindo día que hace hoy” debe devolver { 'que': 2, 'lindo': 1, 'día': 1,
                                                                                  'hace': 1, 'hoy': 1}"""
def contar_palabras(cadena):
    diccionario = {}
    for palabra in cadena.split():
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario