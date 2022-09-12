"""Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.
b) Devuelva la sumatoria y el promedio de los valores.
c) Devuelva una lista con el factorial de cada uno de esos números."""
def es_primo(n):
    #devuelve True si n es primo, False si no lo es
    return n % n == 0 or n % 1 == 0
assert es_primo(5) == True
# a)
def primos(lista):
    for i in range(2, lista + 1):
        primo = True
        for j in range(2, i):
            if i == j:
                break
            elif i % j == 0:
                primos = False
            else:
                continue
        if primo == True:
            print(' ', i, end='')
            contador += 1
    print('\nHay %u números primos.' % contador)

primos(100)


