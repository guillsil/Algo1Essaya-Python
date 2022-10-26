"""2
1
6
3
7
8
4
5
9
10

Escribir una función que reciba un texto y para cada caracter presente en el texto
devuelva la cadena más larga en la que se encuentra ese caracter.

En el caso de que haya más de una cadena posible para elegir, se debe seleccionar la última.

Por ejemplo, si se recibe 'pero que hermoso dia hay' debe devolver:

{'a': 'hay',
 'e': 'hermoso',
 'h': 'hermoso',
 'i': 'dia',
 'r': 'hermoso',
 'u': 'que',
 's': 'hermoso',
 'o': 'hermoso',
 'q': 'que',
 'd': 'dia',
 'y': 'hay',
 'm': 'hermoso',
 'p': 'pero'}"""
def obtener_cadenas_largas_por_caracter(texto):
    diccionario = {}
    texto_sin_espacios = texto.replace(" ", "")
    for caracter in texto_sin_espacios:
        if caracter not in diccionario:
            # buscar la cadena más larga que contenga el caracter
            cadena_mas_larga = ""
            for cadena in texto.split():
                if caracter in cadena:
                    if len(cadena) > len(cadena_mas_larga):
                        cadena_mas_larga = cadena
            diccionario[caracter] = cadena_mas_larga
    return diccionario
print(obtener_cadenas_largas_por_caracter("pero que hermoso dia hay"))
