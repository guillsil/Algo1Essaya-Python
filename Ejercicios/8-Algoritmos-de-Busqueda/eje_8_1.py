"""Ejercicio 8.1. Escribir una función que reciba una lista desordenada y un elemento, que:
a) Busque todos los elementos coincidan con el pasado por parámetro y devuelva la can-
tidad de coincidencias encontradas.
b) Busque la primera coincidencia del elemento en la lista y devuelva su posición.
c) Utilizando la función anterior, busque todos los elementos que coincidan con el pasado
por parámetro y devuelva una lista con las posiciones."""
# a)
def coincidencias(lista, elemento):
    contador = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            contador += 1
    return contador
print(coincidencias([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5], 5))
print(coincidencias(["hola", 2, 3, 4, "juan", 6, 7, 8, "juan", 10, 5], "juan"))
# b)
def primera_coincidencia(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
print(primera_coincidencia([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5], 5))
print(primera_coincidencia(["hola", 2, 3, 4, "juan", 6, 7, 8, "juan", 10, 5], "juan"))
# c)
def todas_coincidencias(lista, elemento):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            posiciones.append(i) #append agrega un elemento al final de la lista
    return posiciones
print(todas_coincidencias([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5], 5))
print(todas_coincidencias(["hola", 2, 3, 4, "juan", 6, 7, 8, "juan", 10, 5], "juan"))