"""Escribir una función recursiva que reciba un número positivo n y devuelva la cantidad de dígitos que tiene."""
def cantidad_digitos(n):
    if n < 10:
        return 1
    return 1 + cantidad_digitos(n // 10)

#prueba
print(cantidad_digitos(1234567891))