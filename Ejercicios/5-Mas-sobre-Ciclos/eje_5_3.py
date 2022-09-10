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
# a)
CONTRASENA = "1234"
def escontraseña(contrasena):
    # Devuelve True si la contraseña es correcta, False si no lo es.
    return contrasena == CONTRASENA
def contrasena():
    ingreso = input("Ingrese la contraseña: ")
    while not escontraseña(ingreso):
        ingreso = input("Ingrese la contraseña: ")
    print("Contraseña correcta")
#b)
def contrasenaB():
    ingreso = input("Ingrese la contraseña: ")
    intentos = 1
    while not escontraseña(ingreso) and intentos < 3:
        ingreso = input("Ingrese la contraseña: ")
        intentos += 1
    if intentos == 3:
        print("Contraseña incorrecta , Intentos agotados")
    else:
        print("Contraseña correcta")
#c)
def contrasenaC():
    ingreso = input("Ingrese la contraseña: ")
    intentos = 1
    while not escontraseña(ingreso) and intentos < 3:
        ingreso = input("Ingrese la contraseña: ")
        intentos += 1
        time.sleep(1*intentos)
    if intentos == 3:
        print("Contraseña incorrecta , Intentos agotados")
    else:
        print("Contraseña correcta")
#d)
def contrasenaD():
    ingreso = input("Ingrese la contraseña: ")
    intentos = 1
    while not escontraseña(ingreso) and intentos < 3:
        ingreso = input("Ingrese la contraseña: ")
        intentos += 1
        time.sleep(1*intentos)
    if intentos == 3:
        return False
    else:
        return True
print(contrasenaD())

