"""Escribir una función que reciba un dígito y un número natural, y decida numé-
ricamente si el dígito se encuentra en la notación decimal del segundo."""
def esta_en(d, n):
    while n > 0:
        if n % 10 == d:
            return True
        n //= 10
    return False
print(esta_en(4, 1234))