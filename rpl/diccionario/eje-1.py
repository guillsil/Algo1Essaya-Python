"""Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
segundos.

Por ejemplo:

>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]
>>> print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }"""
def tuplas_a_diccionario(lista):
    diccionario = {}
    for tupla in lista:
        clave, valor = tupla
        if clave in diccionario:
            diccionario[clave].append(valor)
        else:
            diccionario[clave] = [valor]
    return diccionario