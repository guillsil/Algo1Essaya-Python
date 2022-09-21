"""Escribir una función que reciba un número secreto (entero) y le pregunte un número al usuario. Si el número
ingresado es distinto, debe indicarle si es mayor o menor al número secreto y volver a pedirle otro número.
Si es igual, debe felicitar al usuario y mostrar en cuántos intentos adivinó. No hay un máximo de intentos
pero el usuario debe adivinar para terminar el programa."""
def adivinar_numero(numero_secreto):
    """Adivina el número secreto"""
    numero = int(input("Ingrese un número: "))
    while numero != numero_secreto:
        if numero > numero_secreto:
            print("El número es menor")
        else:
            print("El número es mayor")
        numero = int(input("Ingrese un número: "))
    print("Felicitaciones, adivinaste el número")
adivinar_numero(5)