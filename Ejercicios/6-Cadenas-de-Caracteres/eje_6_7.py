"""Escribir funciones que dadas dos cadenas de caracteres:
a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo, 'cadena'
es una subcadena de 'subcadena'.
b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe 'kde' y 'gnome'
debe devolver 'gnome'."""
# a)
def subcadena(cadena1, cadena2):
    return cadena2 in cadena1
assert subcadena("subcadena", "cadena") == True
# b)
def orden_alfabetico(cadena1, cadena2):
    return cadena1 if cadena1 < cadena2 else cadena2
assert orden_alfabetico("ade", "gnome") == "ade"