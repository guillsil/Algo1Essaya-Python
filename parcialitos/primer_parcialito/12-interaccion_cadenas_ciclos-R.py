"""Escribir una función que realice lo siguiente: - Le pida al usuario que ingrese una contraseña. Luego
debe validar que la misma: - Tenga al menos dos numeros, pero no tenga más números que letras
(a-z, A-Z, no es necesario incluir letras acentuadas o especiales de otros idiomas que no sea el ingles).
- Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres. - Si no ingresa una contraseña
válida debe volver a preguntarle hasta quedarse sin intentos. - Cuando sea válida, se deben devolver la cantidad de
intentos restante. Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1. La cantidad de intentos
es recibida por parametro."""
def validar_cantidad_numeros(cadena):
    """Valida que la cadena tenga al menos dos números y no más números que letras"""
    cantidad_numeros = 0
    cantidad_letras = 0
    for caracter in cadena:
        if caracter.isdigit():
            cantidad_numeros += 1
        elif caracter.isalpha():
            cantidad_letras += 1
    return cantidad_numeros >= 2 and cantidad_numeros <= cantidad_letras

def validar_cantidad_caracteres(cadena):
    """Valida que la cadena tenga alguno de los caracteres permitidos pero no más de tres"""
    cantidad_caracteres = 0
    for caracter in cadena:
        if caracter in "!@~/#":
            cantidad_caracteres += 1
    return cantidad_caracteres > 0 and cantidad_caracteres <= 3

def validar_contrasenia(intentos):
    """Valida la contraseña ingresada por el usuario"""
    while intentos > 0:
        contrasenia = input("Ingrese la contraseña: ")
        if not validar_cantidad_numeros(contrasenia):
            print("La contraseña debe tener al menos dos números y no más números que letras.")
        elif not validar_cantidad_caracteres(contrasenia):
            print("La contraseña debe tener alguno de estos caracteres: !, @, ~, /, # pero no más de tres.")
        else:
            return print(intentos)
        intentos -= 1
    print("Se acabaron los intentos.")
    return -1
validar_contrasenia(3)


