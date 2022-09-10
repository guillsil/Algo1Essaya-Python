"""Escribir funciones que dada una cadena y un caracter:
a) Inserte el caracter entre cada letra de la cadena. Ej: 'separar' y ',' debería devolver
's,e,p,a,r,a,r'
b) Reemplace todos los espacios por el caracter. Ej: 'mi archivo de texto.txt' y '_'
debería devolver 'mi_archivo_de_texto.txt'
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: 'su clave es: 1540' y
'X' debería devolver 'su clave es: XXXX'
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. '2552552550' y '.' debería devolver
'255.255.255.0'"""
# a)
def insertar_caracter(cadena, caracter):
    return caracter.join(cadena) #join() une los elementos de una lista en una cadena
assert insertar_caracter("separar", ",") == "s,e,p,a,r,a,r"
# b)
def reemplazar_espacios(cadena, caracter):
    return cadena.replace(" ", caracter) #replace() reemplaza un caracter por otro
assert reemplazar_espacios("mi archivo de texto.txt", "_") == "mi_archivo_de_texto.txt"
# c)
CARACTERES = "0123456789"
def reemplazar_digitos(cadena, caracter):
    return cadena.translate(cadena.maketrans(CARACTERES, caracter*10)) #translate() reemplaza caracteres #maketrans() crea una tabla de traducción
assert reemplazar_digitos("su clave es: 1540", "X") == "su clave es: XXXX"
# d)
def insertar_caracter_cada_tres(cadena, caracter):
    return caracter.join([cadena[i:i+3] for i in range(0, len(cadena), 3)])
assert insertar_caracter_cada_tres("2552552550", ".") == "255.255.255.0"