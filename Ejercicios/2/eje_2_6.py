"""Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario."""
def mostrarPares(num1, num2):
    for i in range(num1, num2, 2):
        print(i)
def main(num1, num2):
    if num1%2==0:
        mostrarPares(num1, num2)
    else:
        num1 +=1
        mostrarPares(num1, num2)
main(7, 20)




