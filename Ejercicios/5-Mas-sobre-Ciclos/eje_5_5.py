"""Algoritmo de Euclides
a) Implementar el algoritmo de Euclides para calcular el máximo común divisor de dos
números 𝑛 y 𝑚, dado por los siguientes pasos.
1. Teniendo 𝑛 y 𝑚, se obtiene 𝑟, el resto de la división entera de 𝑚/𝑛.
2. Si 𝑟 es cero, 𝑛 es el mcd de los valores iniciales.
3. Se reemplaza 𝑚 ← 𝑛, 𝑛 ← 𝑟, y se vuelve al primer paso.
b) Hacer un seguimiento del algoritmo implementado para los siguientes pares de núme-
ros: (15, 9); (9, 15); (10, 8); (12, 6)."""
# a)
def euclides(n, m):
    r = m % n
    if r == 0:
        return n
    else:
        return euclides(r, n)
print(euclides(15, 9))
print(euclides(9, 15))
print(euclides(10, 8))
print(euclides(12, 6))