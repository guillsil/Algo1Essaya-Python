"""Modificar las funciones anteriores, para que reciban un parámetro que indique la
cantidad máxima de reemplazos o inserciones a realizar."""
# a)
def insertar_caracter(cadena, caracter, parametro):
    return caracter.join(cadena)[:parametro]
assert insertar_caracter("separar", ",", 5) == "s,e,p,a"