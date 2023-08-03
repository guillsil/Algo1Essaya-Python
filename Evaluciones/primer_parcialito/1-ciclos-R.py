"""Dado el siguiente código en Python
for x in range(2, 29, 7):
    print("Valor al inicio de la iteracion:", x)
    x = (x * 2) - 3
    print("Valor al final de la iteracion:", x)
a. Hacer una tabla con los valores de x iniciales y finales de cada iteración. En caso de que el ciclo no termine
nunca, colocar una fila con "...". b. Transformar el ciclo anterior a un ciclo while
    que implemente el mismo comportamiento."""

def algo():
    for x in range(2, 29, 7):
        print("Valor al inicio de la iteracion:", x)
        x = (x * 2) - 3
        print("Valor al final de la iteracion:", x)
algo()
def algo2():
    x = 2
    while x <= 29:
        print("Valor al inicio de la iteracion:", x)
        x = (x * 2) - 3
        print("Valor al final de la iteracion:", x)
        x += 8
algo2()