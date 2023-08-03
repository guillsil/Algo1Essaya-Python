"""Escribir una función que reciba una cadena que contiene un largo número en-
tero y devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
'1234567890', debe devolver '1.234.567.890'."""
def separar_miles(cadena):
    cadena = cadena[::-1]
    
    nueva_cadena = ""
    for i in range(len(cadena)):
        if i % 3 == 0 and i != 0:
            nueva_cadena += "."
        nueva_cadena += cadena[i]
    return nueva_cadena[::-1]
print(separar_miles("1234567890"))
cadena = "1234567890"
print(cadena[::-1])