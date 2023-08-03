"""Escribir una función recursiva que calcule recursivamente el n-ésimo número
triangular (el número 1 + 2 + 3 + ⋯ + 𝑛)."""
def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)
print(triangular(5))

"""numeros triangulares son los que se pueden representar como la suma de los n primeros numeros naturales"""
"""por ejemplo: 
1 = 1
3 = 1 + 2
6 = 1 + 2 + 3
10 = 1 + 2 + 3 + 4
15 = 1 + 2 + 3 + 4 + 5"""