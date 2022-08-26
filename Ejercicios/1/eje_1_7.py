"""Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios.
Ayuda: Investigar acerca del parámetro end de la función print."""

print("Ingresa una Palabra")
palabra = input()
def guillermoMilVeces(palabra):
    for i in range(1, 1001):
        print(palabra + " ", end='')

guillermoMilVeces(palabra)