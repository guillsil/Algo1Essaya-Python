"""Escribir una función que, dados cuatro números, devuelva el mayor producto de
dos de ellos. Por ejemplo, si recibe los números 1-Conceptos-Basicos, 5, -2-Programas-Cencillos, -4-Decisiones debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2-Programas-Cencillos × −4-Decisiones)."""
def maxProducto(num1, num2, num3, num4):
    opc1= num1 * num2
    opc2= num1 * num3
    opc3= num1 * num4
    opc4= num2 * num3
    opc5= num2 * num4
    opc6= num3 * num4
    return max(opc1, opc2, opc3, opc4, opc5, opc6)
print(maxProducto(1, 5, -2, -4))
