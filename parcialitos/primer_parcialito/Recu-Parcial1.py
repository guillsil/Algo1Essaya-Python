"""Un pangrama es una frase o texto que usa todas las letras del alfabeto al menos una vez.
Por ejemplo, la frase
the quick brown fox jumps over the lazy dog es un pangrama en inglés, porque usa todas las letras del
alfabeto inglés al
menos una vez. Escribir una función que recibe una frase y devuelve True si es un pangrama y False en caso
contrario. Nota: ignorar los espacios en blanco y los signos de puntuación. Ejemplo:
>> pangrama("the quick brown fox jumps over the lazy dog")
True
"""
from string import ascii_lowercase
def pangrama(frase):
    """Devuelve True si la frase es un pangrama, False en caso contrario"""
    abc = []
    for c in frase.lower():
        if c in ascii_lowercase:
            abc.append(c)
    return len(set(abc)) == 26
"""print(pangrama("the quick brown fox jumps over the lazy dog"))"""

"""Escribir una funcion que reciba un numero n, y devuelva una matriz triangular superior de dimension n x n, en forma
de lista de listas , cuyos elementos son los numeros del 1 al k en orden (siendo k la cantidad total de números a colocar)
.por ejemplo para n = 4 debe devolver la sguiente matriz:
[[1, 2, 3, 4],
[0, 5, 6, 7],
[0, 0, 8, 9],
[0, 0, 0, 10]]
"""
def crear_matriz(n):
    """Crea una matriz de n x n"""
    matriz = []
    fila = []
    for i in range(n):
        for j in range(n):
            fila.append(0)
        matriz.append(fila)
        fila = []
    return matriz

def matriz_triangular(n):
    """Devuelve una matriz triangular superior de dimension n x n"""
    k = 1
    matriz = crear_matriz(n)
    for i in range(n):
        for j in range(i, n):
            matriz[i][j] = k
            k += 1
    return matriz
print(matriz_triangular(4))

""""Escribir una funcion que le pida al usuario que ingrese un numero. Se debe validar la entrada del usuario
según la siguientes condiciones:
1)Debe ser un Entero  Positivo
2)Debe ser un numero primo
La funcion debe repetir este proceso hasta que el usuario ingrese un numero que cumpla con las dos condicione, o ingrese
un caracter especial de fin (que se reciba como parametro). La funcion debe devolver el numero ingresado por el usuario.
O -1 en caso que haya ingresado el caracter de fin."""
def es_primo(n):
    """Devuelve True si n es primo, False en caso contrario"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def validar(num):
    """Valida que num sea un entero positivo y primo"""
    return num.isdigit() and int(num) > 0 and es_primo(int(num)) and num != ""

def validar_numero():
    """Pide al usuario que ingrese un numero entero positivo y primo"""
    while True:
        num = input("Ingrese un numero entero positivo y primo: ")
        if validar(num):
            return int(num)
        print("Debe ingresar un numero entero positivo y primo.")
print(validar_numero())
