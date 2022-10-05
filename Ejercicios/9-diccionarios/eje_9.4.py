"""Ejercicio 9.4. Escribir una función que reciba un texto y para cada caracter presente en el texto
devuelva la cadena más larga en la que se encuentra ese caracter."""
def cadena_mas_larga(texto):
    """Recibe un texto y para cada caracter presente en el texto devuelve la cadena más larga en la
    que se encuentra ese caracter."""
    palabras = texto.split()
    dic = {}
    for caracter in palabras:
        if caracter.lower() in dic:
            if len(caracter) > len(dic[caracter]):
                dic[caracter] = caracter.lower()
        else:
            dic[caracter] = caracter.lower()
    return dic
print(cadena_mas_larga("Bebe"))