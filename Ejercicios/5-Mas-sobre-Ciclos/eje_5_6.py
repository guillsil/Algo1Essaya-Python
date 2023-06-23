"""Potencias de dos.
a) Escribir una función es_potencia_de_dos que reciba como parámetro un número na-
tural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
b) Escribir una función que, dados dos números naturales pasados como parámetros,
devuelva la suma de todas las potencias de 2 que hay en el rango formado por
esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
es_potencia_de_dos, descripta en el punto anterior."""
# a)
def es_potencia_de_dos(n):
    i = 1
    while i <= n:
        if i == n:
            return True
        i *= 2
    return False
def es_potencia_de_dos2(n):
    while n > 1:
        n /= 2
    return n == 1
print(es_potencia_de_dos(8))
# b)
def suma_potencias_de_dos(n1, n2):
    suma = 0
    for i in range(n1, n2+1):
        if es_potencia_de_dos(i):
            suma += i
    return suma
print(suma_potencias_de_dos(1, 100))