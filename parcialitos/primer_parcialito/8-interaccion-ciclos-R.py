"""Escribir una función que le pida al usuario que ingrese una dirección IPv4 válida. Una dirección
IPv4 válida
consiste de 4 números separados por el caracter . donde cada número está entre 0 y 255. Si el usuario no ingresa
una dirección IPv4 válida, debe volver a pedirle que ingrese una hasta que lo que ingrese sí lo sea.

Al finalizar la ejecucion, debe devolver una cadena con la dirección IPv4 válida. Algunos ejemplos válidos:

192.168.0.1
0.0.0.0
255.255.255.255"""

def validar_ipv4(ipv4):
    """Valida que la dirección IPv4 ingresada sea válida"""
    lista = ipv4.split(".")
    if len(lista) != 4:
        return False
    for numero in lista:
        if not numero.isdigit():
            return False
        if int(numero) < 0 or int(numero) > 255:
            return False
    return True

def pedir_ipv4():
    """Pide al usuario que ingrese una dirección IPv4 válida"""
    while True:
        ipv4 = input("Ingrese una dirección IPv4 válida: ")
        if validar_ipv4(ipv4):
            return ipv4

print(pedir_ipv4())