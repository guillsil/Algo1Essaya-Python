"""Escribir una función que reciba una cantidad de iteraciones de una tirada de dos dados a realizar y
devuelva la cantidad de veces que se observa cada valor.
Nota: utilizar el módulo random para obtener tiradas aleatorias.

Algunos posibles resultados:

>>> contar_resultados_dados(1)
{3: 1, 5: 1}
>>> contar_resultados_dados(1)
{4: 2}
>>> contar_resultados_dados(3)
{2: 1, 5: 1, 4: 2, 6: 1, 3: 1}
>>> contar_resultados_dados(3)
{6: 1, 4: 2, 3: 2, 5: 1}
>>> contar_resultados_dados(3)
{1: 2, 2: 2, 6: 1, 3: 1}"""
import random
def contar_resultados_dados(cantidad):
    diccionario = {}
    for i in range(cantidad):
        resultado = random.randint(1, 6) + random.randint(1, 6)
        if resultado in diccionario:
            diccionario[resultado] += 1
        else:
            diccionario[resultado] = 1
    return diccionario