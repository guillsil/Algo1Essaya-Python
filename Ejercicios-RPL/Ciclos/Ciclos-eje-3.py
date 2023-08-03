"""Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos números n y m, dado por
los siguientes pasos:
1) Teniendo n y m, se obtiene r, el resto de la división entera de m / n.
2)  Si r es cero, n es el mcd de los valores iniciales.
3)  Se reemplaza m <-- n, n <-- r, y se vuelve al primer paso.
Ej:
>> calcular_mcd(4, 8)
4
>> calcular_mcd(24, 60)
12
>> calcular_mcd(11, 17)
1
"""

def calcular_mcd(n, m):
    r = m % n
    if r == 0:
        return n
    else:
        return calcular_mcd(r, n)

print(calcular_mcd(4, 8))
print(calcular_mcd(24, 60))
print(calcular_mcd(11, 17))