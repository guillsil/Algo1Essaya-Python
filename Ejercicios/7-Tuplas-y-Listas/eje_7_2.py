""" Dominó.
a) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en dos tuplas, por ejemplo: (3,4) y (5,4)
b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son
recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las
cadenas."""
# a)
def encajan(ficha1, ficha2):
    return ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]
assert encajan((3, 4), (5, 4)) == True
# b)
def encajan_cadena(ficha1, ficha2):
    ficha1 = tuple(map(int, ficha1.split("-"))) #tuple() convierte una lista en una tupla
    ficha2 = tuple(map(int, ficha2.split("-"))) #map() aplica una función a cada elemento de una lista
    return encajan(ficha1, ficha2)              #split() separa una cadena en una lista de palabras
assert encajan_cadena("3-4", "5-4") == True