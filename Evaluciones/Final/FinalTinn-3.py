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
    matriz_nueva = []
    fila = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        matriz_nueva.append(fila)
        fila = []
    return matriz_nueva

"""2. Escribe una función llamada
filtrar(cola, f) que reciba una cola y una función como
parámetros, y devuelva una nueva cola que contenga los elementos para los cuales la
función
f devuelve
True. La cola original recibida debe quedar vacía al finalizar la
ejecución."""
from cola import Cola
#iterativo
def filtrar(cola, f):
    cola_aux = Cola()
    while not cola.esta_vacia():
        dato = cola.desencolar()
        if f(dato):
            cola_aux.encolar(dato)
        else:
            cola.desencolar
    return cola_aux
#recursivo
def filtrar2(cola, f):
    if cola.esta_vacia():
        return cola
    dato = cola.desencolar()
    if f(dato):
        cola_filtrada = filtrar2(cola, f)
        cola_filtrada.encolar(dato)
    else:
        cola_filtrada = filtrar2(cola, f)
    return cola_filtrada


"""4. Resuelve el siguiente ejercicio de compresión y cadena: (1.5p)
a. Implementar la función
comprimir(cadena) que reciba una cadena y la comprima
mediante el algoritmo RLE.
b. Implementar la función
comprimir_archivo(entrada, salida) que reciba el nombre de
un archivo de texto de entrada y el nombre de un archivo de texto de salida, y comprima
el contenido del archivo de entrada utilizando el algoritmo RLE, guardando el resultado
en el archivo de salida.
Consideraciones:
 En el apartado (a), la función
comprimir recorre la cadena y va contando las
ocurrencias consecutivas de cada carácter para crear la cadena comprimida.
 En el apartado (b), la función
comprimir_archivo lee el contenido del archivo
de entrada, lo comprime utilizando la función
comprimir y guarda el resultado
en el archivo de salida.
 Asegúrate de manejar adecuadamente las excepciones y casos de error, como
la falta de los archivos especificados."""
