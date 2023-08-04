"""1. Resuelve los siguientes ejercicios de matrices: (1.5p)
a. Escribe una función llamada
obtener_promedio_matriz(matriz) que reciba una matriz
de números enteros y retorne el promedio de todos los elementos.
La matriz será representada como una lista de listas, donde cada sublista representa una
fila de la matriz y contiene números enteros. Asegúrate de que la matriz tenga al menos
un elemento antes de calcular el promedio.
Consideraciones:
 La función debe devolver el resultado del promedio con un decimal de
precisión.
 Si la matriz está vacía, la función debe retornar
“None”.
 Puedes asumir que todas las sublistas tendrán la misma cantidad de elementos.
b. Escribe una función llamada
matriz_transpuesta(matriz) que reciba una matriz
cuadrada (misma cantidad de filas y columnas) representada como una lista de listas y
retorne su matriz transpuesta.
La matriz transpuesta de una matriz se obtiene intercambiando sus filas por columnas.
Consideraciones:
 Puedes asumir que la matriz siempre será cuadrada.
 La función debe retornar una nueva matriz transpuesta y no modificar la matriz
original."""
#a
def obtener_pomedio(matriz):
    contador = 0
    cant = 0
    for fila in matriz:
        for x in fila:
            contador += x
            cant += 1

    if contador == 0:
        raise ValueError("Matriz Vacia")
    resultado = (contador / cant)
    return f"{resultado:.1f}"

#b
def matriz_transpuesta(matriz):
    matriz_n = []
    fila_n = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            fila_n.append(matriz[j][i])
        matriz_n.append(fila_n)
        fila_n = []
    return matriz_n

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(obtener_pomedio(matriz))
