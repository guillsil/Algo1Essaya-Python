"""Escribir una función que reciba una palabra y devuelva una lista con todas las rotaciones posibles de esa palabra.
Ejemplo:
rotaciones('rotar') → ['rotar','otarr','tarro','arrot','rrota']
Aclaración: Para ser considerada una rotación, las letras deben mantener el orden relativo (en forma circular).
Ejemplo: 'torra' no es una rotación posible a partir de 'rotar'."""
def rotaciones(palabra):
    """Devuelve una lista con todas las rotaciones posibles de la palabra."""
    lista = []
    for i in range(len(palabra)):
        lista.append(palabra[i:] + palabra[:i])
    return lista
print(rotaciones("rotar"))

palabra = "rotar"
print(palabra[1:] )