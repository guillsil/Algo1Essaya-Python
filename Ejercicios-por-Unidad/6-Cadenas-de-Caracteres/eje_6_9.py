"""Implementar la función pedir_entero(mensaje, min, max), que debe imprimir
el mensaje y luego esperar a que el usuario ingrese un valor. Si el valor ingresado no es un
número entero, o no es un número entre min y max (inclusive), se le debe avisar al usuario y
pedir el ingreso de otro valor. Una vez que el usuario ingresa un valor válido, la función lo debe
devolver.
Ejemplo:
z = pedir_entero("¿Cuál es tu número favorito?", -50, 50)
¿Cuál es tu número favorito? [-50..50]:
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: hola
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: -60
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: 51
Por favor ingresa un número entre -50 y 50.
¿Cuál es tu número favorito? [-50..50]: -16
-16"""
def pedir_entero(mensaje, min, max):
    while True:
        try:
            x = int(input(mensaje))
            if x < min or x > max:
                print("Por favor ingresa un número entre {} y {}.".format(min, max)) #format() formatea una cadena
            else:
                return x
        except ValueError: #ValueError se produce cuando una función int() no puede convertir un valor a entero
            print("Por favor ingresa un número entre {} y {}.".format(min, max))
pedir_entero("¿Cuál es tu número favorito?", -50, 50)