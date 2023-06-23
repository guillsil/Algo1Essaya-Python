"""Escribir una función que, dados cuatro números, devuelva el mayor producto de
dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −)."""
def maxProducto(num1, num2, num3, num4):
    return max(num1*num2, num1*num3, num1*num4, num2*num3, num2*num4, num3*num4)
print(maxProducto(1, 5, -2, -9))
