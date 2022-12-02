"""Sea la siguiente operación, aplicable a cualquier número entero positivo:

    Si el número es par, se divide por 2.
    Si el número es impar, se multiplica por 3 y se suma 1.

La conjetura de Collatz dice que, para cualquier número con el que comencemos, si aplicamos la operación
sucesivamente, siempre alcanzaremos el número 1. Escribir la función recursiva collatz(n) que imprime la secuencia de
operaciones comenzando desde el número n, y terminando en el número 1. Ejemplo: collatz(5) → 5 16 8 4 2 1

"""
def collatz(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(n * 3 + 1)

print(collatz(5))
print(collatz(4))