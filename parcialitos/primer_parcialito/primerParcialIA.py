"""
#1
Escribe una función llamada maximos_puntajes que tome una matriz representada como una lista de listas, donde cada elemento de la matriz es una tupla que representa el puntaje de un país con el formato (<Pais>, <Puntaje>). La función debe devolver una lista con todos los países que tengan el mayor puntaje para su columna. En caso de empate, se puede elegir cualquiera. Por ejemplo, para la matriz:"""

def maximos_puntajes(matriz):
    lista_maximos = []
    
    # Recorremos cada columna de la matriz
    for columna in range(len(matriz[0])):
        mayor_puntaje = matriz[0][columna][1]
        
        # Buscamos el mayor puntaje en la columna actual
        for fila in range(1, len(matriz)):
            if matriz[fila][columna][1] > mayor_puntaje:
                mayor_puntaje = matriz[fila][columna][1]
        
        # Agregamos a la lista los países con el mayor puntaje de la columna
        for fila in range(len(matriz)):
            if matriz[fila][columna][1] == mayor_puntaje:
                lista_maximos.append(matriz[fila][columna][0])
    
    return lista_maximos

# Ejemplo de matriz
matriz = [[("Argentina", 10), ("Brasil", 20), ("Alemania", 30)],
          [("Portugal", 20), ("Dinamarca", 30), ("Paraguay", 40)],
          [("Croacia", 30), ("Brasil", 40), ("Honduras", 50)]]

# Llamamos a la función para obtener los países con los mayores puntajes por columna
lista_maximos = maximos_puntajes(matriz)

# Imprimimos los resultados
for pais in lista_maximos:
    print(pais)

