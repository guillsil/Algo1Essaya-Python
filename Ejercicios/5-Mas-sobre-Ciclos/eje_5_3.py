"""Manejo de contraseñas
a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usua-
rio la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de inten-
tos.
c) Modificar el programa anterior para que después de cada intento agregue una pausa
cada vez mayor, utilizando la función sleep del módulo time.
d) Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False)."""
import time
CONTRASENA = "1234"
#a)
"""

def contrasena():
    while True:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == CONTRASENA:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta")
            continue
contrasena()"""

#b)
MAXINTENTOS = 3
"""def contrasenaB():
    intentos = 0
    while True and intentos < MAXINTENTOS:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == CONTRASENA:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta")
            intentos += 1
            continue
    if intentos == MAXINTENTOS:
        print("Intentos agotados")

contrasenaB()"""

#c)
"""def contrasenaC():
    intentos = 0
    while True and intentos < MAXINTENTOS:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == CONTRASENA:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta")
            intentos += 1
            time.sleep(1*intentos)
            continue
    if intentos == MAXINTENTOS:
        print("Intentos agotados")

contrasenaC()"""

#d)
def contrasenaD():
    intentos = 0
    while True and intentos < MAXINTENTOS:
        contrasenia = input("Ingrese la contraseña: ")
        if contrasenia == CONTRASENA:
            print("Contraseña correcta")
            return True
        else:
            print("Contraseña incorrecta")
            intentos += 1
            time.sleep(1*intentos)
            continue

    
    if intentos == MAXINTENTOS:
        print("Intentos agotados")

contrasenaD()
