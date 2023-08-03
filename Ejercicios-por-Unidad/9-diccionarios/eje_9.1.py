"""Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario
en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los
segundos.
Por ejemplo:
>>> l = [ ('Hola', 'don Pepito'), ('Hola', 'don Jose'),
('Buenos', 'días') ]
>>> print(tuplas_a_diccionario(l))
{ 'Hola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }"""
def tuplas_a_diccionario(tuplas):
    diccionario = {}
    for clave, valor in tuplas:
        diccionario[clave] = diccionario.get(clave, []) + [valor]
    return diccionario
print(tuplas_a_diccionario([ ('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Buenos', 'días') ]))
