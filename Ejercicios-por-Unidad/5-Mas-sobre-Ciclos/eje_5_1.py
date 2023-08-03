"""Escribir un programa que permita al usuario ingresar un conjunto de notas, pre-
guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente."""

def promedio():
    notas = []
    while True:
        nota = int(input("Ingrese una nota: "))
        notas.append(nota)
        seguir = input("Desea ingresar más notas? (s/n): ")
        if seguir == "n":
            break
    return sum(notas) / len(notas)
print(promedio())