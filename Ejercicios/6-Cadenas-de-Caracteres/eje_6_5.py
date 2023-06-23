"""Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
devolver 'USB'.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
debe devolver 'Antes ayer'"""
# a)
def primera_letra(cadena):
    primeraLetra = ""
    #split() separa la cadena en palabras
    for i in cadena.split():
        primeraLetra += i[0]
    return primeraLetra
print(primera_letra("Universal Serial Bus"))
# b)
def primera_letra_mayuscula(cadena):
    primera_letra = ""
    for i in cadena.split():
        primera_letra += i[0].upper() + i[1:] + " "
    return primera_letra
print(primera_letra_mayuscula("república argentina"))
# c)
def palabras_con_a(cadena):
    palabras = ""
    for palabra in cadena.split():
        if palabra[0].lower() == "a":
            palabras += palabra + " "
    return palabras
print(palabras_con_a("Antes de ayer"))