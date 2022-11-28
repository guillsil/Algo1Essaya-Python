"""Escribir una función ajustar_linea() que recibe una cadena y un número n, y devuelva una lista con la cadena
original partida en multiples cadenas de tamaño n. La unica cadena con tamaño menor a n es la ultima
(si no hay suficientes caracteres). Ejemplos:
ajustar_linea('Algoritmos', 5)
  => ['Algor', 'itmos']
ajustar_linea('Algoritmos y programacion I', 8)
  => ['Algoritm', 'os y pro', 'gramacio', 'n I']"""

def ajustar_linea(cadena, n):
    """Devuelve una lista con la cadena original partida en multiples cadenas de tamaño n."""
    lista = []
    for i in range(0, len(cadena), n):
        lista.append(cadena[i:i+n])
    return lista
print(ajustar_linea('Algoritmos', 5))
print(ajustar_linea('Algoritmos y programacion I', 8))