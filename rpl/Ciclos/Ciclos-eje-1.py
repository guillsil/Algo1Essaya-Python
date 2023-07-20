"""Escribir un programa que permita al usuario ingresar un conjunto de notas, preguntando a cada paso si desea
ingresar más notas, e imprimiendo el promedio correspondiente.
Ejemplo:
>> Ingrese una nota: 6
>> Desea ingresar mas notas? (s/n): s
>> Ingrese una nota: 7
>> Desea ingresar mas notas? (s/n): s
>> Ingrese una nota: 8
>> Desea ingresar mas notas? (s/n): s
>> Ingrese una nota: 9
>> Desea ingresar mas notas? (s/n): n
>> El promedio es: 7.5
"""

def main():
    notas = []
    while True:
        nota = int(input("Ingrese una nota: "))
        notas.append(nota)
        respuesta = input("Desea ingresar mas notas? (s/n): ")
        if respuesta == "n":
            break
    print("El promedio es: ", sum(notas) / len(notas))

main()