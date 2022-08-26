"""Escribir funciones que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número natural 𝑛, imprimir su tabla de multiplicar."""
def fusion1(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    division = num1 / num2
    multiplicacion = num1 * num2
    print("El resultado de la suma es:" + str(suma))
    print("El resultado de la resta es:" + str(resta))
    print("El resultado de la division es:" + str(division))
    print("El resultado de la multiplicacion es:" + str(multiplicacion))

def tablaMultiplicacion(num):
    for i in range(1, 11):
        print(str(num) + "x" + str(i) + "=" + str(num*i))

tablaMultiplicacion(7)