"""Escribir una función que reciba dos secuencias y devuelva una lista con los elementos comunes a ambas,
sin repetir ninguno. Ejemplo: f([7, 9, 7, 1], [6, 9, 7]) → [7, 9]"""
def comunes(a, b):
    comunes = []
    for elemento in a:
        if elemento in b and elemento not in comunes:
            comunes.append(elemento)
    return comunes
print(comunes([7, 9, 7, 1], [6, 9, 7]))