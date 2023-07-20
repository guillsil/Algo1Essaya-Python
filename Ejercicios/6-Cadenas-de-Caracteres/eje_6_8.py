"""Escribir una función que reciba una cadena de unos y ceros (es decir, un número
en representación binaria) y devuelva el valor decimal correspondiente."""
def binario_a_decimal(cadena):
    #convertir un numero binario a decimal
    return int(cadena, 2)  #int() convierte una cadena a enteros
assert binario_a_decimal("1001") == 9

def decimal_a_binario(cadena):
    #convertir un numero decimal a binario
    return bin(int(cadena))  #bin() convierte un entero a binario
assert decimal_a_binario("100") == "01100100"