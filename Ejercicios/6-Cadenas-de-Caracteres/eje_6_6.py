"""Escribir funciones que dada una cadena de caracteres:
a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
'logaritmos' debe devolver 'lgrtms'.
b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
devolver 'i ooae'.
c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
devolver 'vistaerou'.
d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un pa-
líndromo (se lee igual de izquierda a derecha que de derecha a izquierda)."""
# a)
def consonantes(cadena):
    return "".join([i for i in cadena if i not in "aeiouAEIOU"])
assert consonantes("algoritmos") == "lgrtms"
assert consonantes("logaritmos") == "lgrtms"
# b)
def vocales(cadena):
    return "".join([i for i in cadena if i in "aeiouAEIOU"])
assert vocales("sin consonantes") == "iooae"
# c)
def siguiente_vocal(cadena):
    return cadena.translate(cadena.maketrans("aeiouAEIOU", "eiouaEIOUA")) #makestrans() crea una tabla de traducción
assert siguiente_vocal("vestuario") == "vistaerou"
# d)
def palindromo(cadena):
    return cadena == cadena[::-1] #[::-1] invierte una cadena
assert palindromo("radar") == True