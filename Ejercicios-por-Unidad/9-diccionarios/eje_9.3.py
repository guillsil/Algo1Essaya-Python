"""Continuación de la agenda.
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena ”*”, para salir del programa.
"""
#a)
def agenda():
    """Vaya solicitando al usuario que ingrese nombres. Si el nombre se encuentra en la
    agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
    Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente."""
    agenda = {}
    while True:
        nombre = input("Ingrese un nombre: ")
        if nombre == "*":
            break
        elif nombre in agenda:
            print("El teléfono de {} es {}".format(nombre, agenda[nombre]))
            opcion = input("¿Desea modificar el teléfono? (s/n): ")
            if opcion == "s":
                agenda[nombre] = input("Ingrese el nuevo teléfono: ")
        else:
            agenda[nombre] = input("Ingrese el teléfono: ")
    return agenda
print(agenda())


