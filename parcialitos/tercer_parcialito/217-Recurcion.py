"""Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de apariciones de c en s."""
#para ayudarme a pensar de forma recursiva lo pienso primero en modo iterativa
def cantidad_de_apariciones(cadena, caracter):
    contador = 0
    for c in cadena:
        if c == caracter:
            contador += 1
    return contador

#recursiva
def cantidad_de_apariciones(cadena, caracter):
    #caso bases (si la cadena esta vacia, no hay apariciones)
    if len(cadena) == 0:
        return 0
    #caso recursivo
    if cadena[0] == caracter:
        return 1 + cantidad_de_apariciones(cadena[1:], caracter)
    else:
        return cantidad_de_apariciones(cadena[1:], caracter)
    
    
cadena = "hola mundo"
print(cadena[1:])


