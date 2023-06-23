"""Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
'reflejoojelfer'."""
CADENA = "Hola Mundo"
#a)
def dos_primeros(cadena):
    return cadena[:2]
assert dos_primeros(CADENA) == "Ho"
#b)
def tres_ultimos(cadena):
    return cadena[-3:]
print(tres_ultimos(CADENA))
#c)
def cada_dos(cadena):
    return cadena[::2]
assert cada_dos(CADENA) == "Hl ud"
#d)
def inverso(cadena):
    return cadena[::-1]
assert inverso(CADENA) == "odnuM aloH"
#e)
def inverso_y_normal(cadena):
    return cadena + inverso(cadena) #inverso(cadena) devuelve la cadena al reves
assert inverso_y_normal(CADENA) == "Hola MundoodnuM aloH"