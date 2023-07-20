"""Escribir una función que reciba dos cadenas, texto y palabra, y devuelva una cadena igual a texto pero con
todas las ocurrencias de palabra censuradas (es decir, reemplazados sus caracteres por *).
Ejemplo: censurar(“Un tete a tete con Tete”, “tete”) → “Un **** a **** con ****” (notar que tanto tete como
Tete fueron censuradas).
"""
def censurar(texto, palabra):
    """Devuelve el texto censurado."""
    texto = texto.split()
    for i in range(len(texto)):
        if texto[i].lower() == palabra.lower():
            texto[i] = "*" * len(texto[i])
    return " ".join(texto)
print(censurar("Un tete a tete con Tete", "tete"))