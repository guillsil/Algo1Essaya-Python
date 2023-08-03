"""Escribir dos funciones mutualmente recursivas par(n) e impar(n) que deter-
minen la paridad del numero natural dado, conociendo solo que:
• 1 es impar.
• Si un número es impar, su antecesor es par; y viceversa."""
def impar(n):
    if n == 0:
        return False
    else:
        return par(n - 1)
def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)
print(impar(0))
print(impar(1))
print(impar(2))
print(impar(3))
print(impar(4))
print(impar(5))