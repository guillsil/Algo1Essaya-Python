"""Escribir una implementación propia de la función abs, que devuelva el valor ab-
soluto de cualquier valor que reciba."""
def abs(n):
    if n < 0:
        n = n * -1
    return n

print(abs(-5))