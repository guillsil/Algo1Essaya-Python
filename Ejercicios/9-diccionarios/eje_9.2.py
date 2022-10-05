"""Diccionarios usados para contar.
a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
dena de texto, y los devuelva en un diccionario.
c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
dados.
Nota: utilizar el módulo random para obtener tiradas aleatorias."""
# a)
def contar_palabras(cadena):
    """Recibe una cadena y devuelve un diccionario con la cantidad de apariciones de
    cada palabra en la cadena."""
    palabras = cadena.split()
    dic = {}
    for palabra in palabras:
        if palabra.lower() in dic:
            dic[palabra.lower()] += 1
        else:
            dic[palabra.lower()] = 1
    return dic
print(contar_palabras("Qué lindo día que hace hoy"))
#b)
def contar_caracteres(cadena):
    """Recibe una cadena y devuelve un diccionario con la cantidad de apariciones de
    cada caracter en la cadena."""
    dic = {}
    for caracter in cadena:
        if caracter.lower() in dic:
            dic[caracter.lower()] += 1
        else:
            dic[caracter.lower()] = 1
    return dic
print(contar_caracteres("Qué lindo día que hace hoy"))
#c)
import random
def contar_tiradas(n):
    """Recibe una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelve
    la cantidad de veces que se observa cada valor de la suma de los dos dados."""
    dic = {}
    for i in range(n):
        tirada = random.randint(1,6) + random.randint(1,6)
        if tirada in dic:
            dic[tirada] += 1
        else:
            dic[tirada] = 1
    return dic
print(contar_tiradas(10))
