"""Escribir una función que reciba una lista de números no ordenada, que:
a) Devuelva el valor máximo
b) Devuelva una tupla que incluya el valor máximo y su posición.
c) ¿Qué sucede si los elementos son cadenas de caracteres?"""
# a)
def maximo(lista):
    maximo = lista[0]
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo
print(maximo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]))
print(maximo(["hola", "juan", "pedro", "maria", "ana"]))
# b)
def maximo_y_posicion(lista):
    maximo = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i
    return (maximo, posicion)
print(maximo_y_posicion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]))
print(maximo_y_posicion(["hola", "juan", "pedro", "maria", "ana"]))
# c)
# Si los elementos son cadenas de caracteres, se comparan por orden alfabético, por lo que
# el máximo es el último elemento de la lista.
