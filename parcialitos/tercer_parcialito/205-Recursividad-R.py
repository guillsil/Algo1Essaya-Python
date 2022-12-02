"""El algoritmo de Euclides se utiliza para calcular el máximo común divisor entre dos números. El mismo consiste
en lo siguiente:
    Dados dos números enteros, $a$ y $b$, se divide el número mayor ($a$) por el menor ($b$) y se obtiene el resto de
    la división entera ($r$).
    En caso de que el resto ($r$) de la división sea cero, el divisor ($b$) es el m.c.d.
    En otro caso, se vuelve al primer paso, dividiendo al divisor ($b$) por el resto ($r$).

Escribir en Python una función recursiva que devuelva el máximo común divisor de un número mediante el algoritmo de Euclides.
"""
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
print(mcd(12, 18))