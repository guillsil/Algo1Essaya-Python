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
    consonantes = ""
    for letra in cadena:
        if letra not in "aeiouAEIOU":
            consonantes += letra
    return consonantes
print(consonantes("algoritmos"))

# b)
def vocales(cadena):
    vocales = ""
    for letra in cadena:
        if letra in "aeiouAEIOU":
            vocales += letra
    return vocales
print(vocales("sin consonantes"))
# c)
def siguiente_vocal(cadena):
    vocales = "aeiouAEIOU"
    siguiente = ""
    for letra in cadena:
        if letra in vocales:
            siguiente += vocales[(vocales.index(letra) + 1) % len(vocales)]
        else:
            siguiente += letra
    return siguiente
# d)
def palindromo(cadena):
    cadena = cadena.replace(" ", "")
    return cadena == cadena[::-1]