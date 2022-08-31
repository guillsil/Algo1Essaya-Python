"""Escribir un programa que imprima por pantalla todas las fichas de dominó, de
una por línea y sin repetir."""
def main():
    for i in range(1,10):
        for j in range(1,10):
            print(i,j)
main()