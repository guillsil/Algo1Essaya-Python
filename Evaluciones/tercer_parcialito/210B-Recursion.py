"""Realizar una función recursiva en Python que reciba un número entero y devuelva el producto de sus dígitos. Ejemplo: producto_digital(356) → 90, pues $3 \cdot 5 \cdot 6 = 90$."""
#iterativo
def producto_digital(numero):
    numero = str(numero)
    producto = 1
    for digito in numero:
        producto *= int(digito)
    return producto

print(producto_digital(356))

#RECURSIVO
def producto_digital2(numero, producto=1):
    numero = str(numero)
    if len(numero) == 0:
        return producto
    if len(numero) != 0:
        producto *= int(numero[0])
        return producto_digital2(numero[1:], producto)
  

print(producto_digital2(356))