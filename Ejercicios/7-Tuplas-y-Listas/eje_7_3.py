"""Campaña electoral
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima
el mensaje Estimado <nombre>, vote por mí.
b) Escribir una función que reciba una tupla con nombres, una posición de origen p y una
cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir
de la posición p.
c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,
para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género"""
# a)
def campaña_electoral(nombres):
    for nombre in nombres:
        print("Estimado", nombre, ", vote por mí.")
"""campaña_electoral(("Juan", "Pedro", "María", "Ana", "Guillermo"))"""
# b)
def campana_electoral_con_posicion(nombres, p, n):
    for nombre in nombres[p:p+n]:
        print("Estimado", nombre, ", vote por mí.")
"""campana_electoral_con_posicion(("Juan", "Pedro", "María", "Ana", "Guillermo"), 1, 3)"""
# c)
def campaña_electoral_genero1(nombres):
    for nombre, genero in nombres:
        print("Estimada" if genero == "F" else "Estimado", nombre, ", vote por mí.")
campaña_electoral_genero1((("Juan", "M"), ("Pedro", "M"), ("María", "F"), ("Ana", "F"), ("Guillermo", "M")))
def campaña_electoral_genero2(nombres, p, n):
    for nombre, genero in nombres[p:p+n]:
        print("Estimada" if genero == "F" else "Estimado", nombre, ", vote por mí.")
campaña_electoral_genero2((("Juan", "M"), ("Pedro", "M"), ("María", "F"), ("Ana", "F"), ("Guillermo", "M")), 1, 3)


