"""Modificar el programa anterior para que pueda generar fichas de un juego que
puede tener números de 0 a 𝑛."""

def main(n):
    for i in range(0, n+1):
        for j in range(i, n+1):
            print(i, j)
main(5)

