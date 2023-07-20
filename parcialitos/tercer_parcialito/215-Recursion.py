"""Sea la siguiente operación, aplicable a cualquier número entero positivo:

    Si el número es par, se divide por 2.
    Si el número es impar, se multiplica por 3 y se suma 1.

La conjetura de Collatz dice que, para cualquier número con el que comencemos, si aplicamos la operación sucesivamente, siempre alcanzaremos el número 1. Escribir la función recursiva collatz(n) que imprime la secuencia de operaciones comenzando desde el número n, y terminando en el número 1. Ejemplo: collatz(5) → 5 16 8 4 2 1
"""
#iterativo
def collatz(n):
    cadena = "collatz "
    cadena += f"{int(n)}: "
    while n != 1:
        if n % 2 == 0:
            cadena += f"{int(n)} "
            n = n /2
        else:
            cadena += f"{int(n)} "
            n = (n * 3) + 1
    return cadena + f"{int(n)}"
print(collatz(5))

#recursivo
def collatz2(n):
    print(n, end=' ')
    if n == 1:
        return
    elif n % 2 == 0:
        collatz2(n // 2)
    else:
        collatz2(3 * n + 1)

collatz2(5)
    

