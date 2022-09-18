"""Funciones que reciben funciones.
a) Escribir una funcion llamada map, que reciba una función y una lista y devuelva la lista
que resulta de aplicar la función recibida a cada uno de los elementos de la lista recibida.
b) Escribir una función llamada filter, que reciba una función y una lista y devuelva una
lista con los elementos de la lista recibida para los cuales la función recibida devuelve un
valor verdadero.
c) ¿En qué ejercicios de esta guía podría haber utilizado estas funciones?"""
# a)
def map(funcion, lista):
    for i in range(len(lista)):
        lista[i] = funcion(lista[i])
    return lista
"""print(map(lambda x: x**2, [1, 2, 3, 4, 5]))""" #lambda x: x**2 es una función anónima
# b)
def filter(funcion, lista):
    new_list = []
    for i in range(len(lista)):
        if funcion(lista[i]):
            new_list.append(lista[i])
    return new_list
print(filter(lambda x: x%2 == 0, [1, 2, 3, 4, 5])) #lambda x: x%2 == 0 es una función anónima
# c)
# En el ejercicio 7.10hacer, en la función producto_de_matrices, se podría haber utilizado