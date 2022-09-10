"""Escribir una función que dada una cadena de caracteres, devuelva:
a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
devolver 'USB'.
b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
'república argentina' debe devolver 'República Argentina'.
c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
debe devolver 'Antes ayer'"""
# a)
def primera_letra(cadena):
    return "".join([i[0] for i in cadena.split()]) #split() separa una cadena en una lista de palabras
assert primera_letra("Universal Serial Bus Car") == "USBC"
# b)
def primera_letra_mayuscula(cadena):
    return " ".join([i.capitalize() for i in cadena.split()]) #capitalize() pone la primera letra en mayúscula
assert primera_letra_mayuscula("república argentina") == "República Argentina"
# c)
def palabras_con_a(cadena):
    return " ".join([i for i in cadena.split() if i[0] == "A" or i[0] == "a"])
print(palabras_con_a("Antes que Nadie de ayer"))