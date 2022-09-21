"""Se pide realizar un programa que le pida al usuario un texto (formado únicamente por letras y espacios) y
una letra, y cuente el total de palabras que inician o terminan con esa letra."""
def contar_palabras(texto, letra):
    """Cuenta las palabras que inician o terminan con la letra"""
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        if palabra[0] == letra or palabra[-1] == letra:
            contador += 1
    return contador
print(contar_palabras("hola como estas", "a"))