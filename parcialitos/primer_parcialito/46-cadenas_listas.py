"""Escribir una función que traduce una oración en español (formada por palabras en minúsculas, separadas por
espacios) a latín de los cerdos. Cada palabra se traduce moviendo la primera letra al final y agregando
"ay". Ejemplo: f("hola mundo") → "olahay undomay"""
def traduccion(cadena):
    """Traduce una oración en español a latín de los cerdos"""
    palabras = cadena.split()
    for i in range(len(palabras)):
        palabras[i] = palabras[i][1:] + palabras[i][0] + "ay"
    return ' '.join(palabras)
print(traduccion("hola mundo"))
