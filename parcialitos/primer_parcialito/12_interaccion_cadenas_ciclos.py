"""Escribir una función que realice lo siguiente: - Le pida al usuario que ingrese una contraseña. Luego
debe validar que la misma: - Tenga al menos dos numeros, pero no tenga más números que letras
(a-z, A-Z, no es necesario incluir letras acentuadas o especiales de otros idiomas que no sea el ingles).
- Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres. - Si no ingresa una contraseña
válida debe volver a preguntarle hasta quedarse sin intentos. - Cuando sea válida, se deben devolver la cantidad de
intentos restante. Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1. La cantidad de intentos
es recibida por parametro."""
def validar_contrasenia(intentos):
    """Valida la contraseña ingresada por el usuario"""
    intentos -=1
    numeros = 0
    caracteres_especiales = 0
    contrasenia = input("Ingrese una contraseña: ")
    while intentos > 0:
        for caracter in contrasenia:
            if caracter.isdigit():
                numeros += 1
            elif caracter in ("!", "@", "~", "/", "#"):
                caracteres_especiales += 1
        if numeros >= 2 and numeros < (len(contrasenia) - numeros) and caracteres_especiales <= 3:
            return intentos
        else:
            intentos -= 1
            numeros = 0
            caracteres_especiales = 0
            contrasenia = input("Contraseña inválida. Ingrese una nueva contraseña: ")
    print("Se acabaron los intentos")
    return -1
validar_contrasenia(3)


