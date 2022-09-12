"""Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Ini-
cial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
nombre, luego la inicial con un punto, y luego el apellido."""
LISTA = [("González", "Juan", "P"), ("Pérez", "Ana", "M"), ("García", "María", "L")]
def nombres_completos(lista):
    return [f"{nombre} {inicial}. {apellido}" for apellido, nombre, inicial in lista]

print(nombres_completos(LISTA))