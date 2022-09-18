"""Plegado de un texto. Escribir una función que reciba un párrafo de texto (pala-
bras separadas por espacios) y una longitud 𝑛, y devuelva una lista conteniendo líneas de texto
de longitud máxima 𝑛. Las líneas deben ser cortadas correctamente en los espacios (sin cortar
las palabras). Asumir que ninguna palabra tiene longitud mayor a 𝑛. Ejemplo:
# >>> plegar('El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado
↪ un saxofón', 20)
['El viejo Señor Gómez', 'pedía queso, kiwi y', 'habas, pero le ha', 'tocado un
↪ saxofón']"""
def plegar(texto, n):
    palabras = texto.split()
    lineas = []
    linea = ''
    for palabra in palabras:
        if len(linea) + len(palabra) + 1 <= n:
            linea += palabra + ' '
        else:
            lineas.append(linea)
            linea = palabra + ' '
    lineas.append(linea)
    return lineas
print(plegar('El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón', 10))