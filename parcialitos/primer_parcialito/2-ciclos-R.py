"""Escribir una función que recibe un número entero $n$ e imprime un tablero de ajedrez de tamaño
$N \times
N$. Por ejemplo, el tablero deberá imprimirse de la siguiente forma para un tablero de $N = 3$:
b n b
n b n
b n b
Nota: b denota un casillero blanco, n denota un casillero negro"""
def imprimir_tablero(n):
    """Imprime un tablero de ajedrez de tamaño n x n"""
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("b", end="")
            else:
                print("n", end="")
        print()
imprimir_tablero(10)

def imprimir_tablero2(n):
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("b", end="")
            else:
                print("n", end="")
        print("")

imprimir_tablero2(4)