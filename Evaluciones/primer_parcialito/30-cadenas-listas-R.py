"""Un bigrama es una secuencia de dos palabras contiguas dentro de un texto. Escribir una función que reciba un texto
y devuelva una lista con todos sus bigramas. Los mismos deberán estar representados con una tupla
(<palabra1>, <palabra2>). Ejemplo:
>> obtener_bigramas(“Uno se alegra de resultar útil”)
[(“Uno”, “se”), (“se”, “alegra”), (“alegra”, “de”), (“de”, “resultar”), (“resultar”, “útil”)]"""
def obtener_bigramas(texto):
    """Devuelve una lista con todos los bigramas del texto."""
    lista = []
    palabras = texto.split()
    for i in range(len(palabras) - 1):
        lista.append((palabras[i], palabras[i + 1]))
    return lista
print(obtener_bigramas("Uno se alegra de resultar útil"))