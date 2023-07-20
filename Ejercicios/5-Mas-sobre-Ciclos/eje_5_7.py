""" Números perfectos y números amigos
a) Escribir una función que devuelva la suma de todos los divisores de un número 𝑛, sin
incluirlo.
b) Usando la función anterior, escribir una función que imprima los primeros 𝑚 números
tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros 𝑚 números
perfectos).
c) Usando la primera función, escribir una función que imprima las primeras 𝑚 parejas
de números (𝑎, 𝑏), tales que la suma de los divisores de 𝑎 es igual a 𝑏 y la suma de los
divisores de 𝑏 es igual a 𝑎 (es decir las primeras 𝑚 parejas de números amigos).
d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecu-
ción."""
# a)
def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma
assert suma_divisores(6) == 6
# b)
def numeros_perfectos(m):
    i = 1
    while m > 0:
        if suma_divisores(i) == i:
            print(i)
            m -= 1
        i += 1
# c)
def numeros_amigos(m):
    i = 1
    while m > 0:
        if suma_divisores(i) == i:
            j = suma_divisores(i)
            if suma_divisores(j) == i:
                print(i, j)
                m -= 1
        i += 1
numeros_amigos(20)
