"""Escribir una función que reciba una cadena que contiene un largo número en-
tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'."""
def separar_miles(cadena):
    return ".".join([cadena[i:i+3] for i in range(0, len(cadena), 3)])
assert separar_miles("1234567890") == "123.456.789.0"