"""Agenda simplificada
Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
Debe devolver una lista con todas las tuplas encontradas."""
def buscar(cadena, lista):
    lista_encontrados = []
    for i in range(len(lista)):
        if cadena in lista[i][0]:
            lista_encontrados.append(lista[i])
    return lista_encontrados
agenda = [("Juan Perez", "12345678"), ("Maria Lopez", "87654321"), ("Juan Gomez", "11111111")]
print(buscar("Juan", agenda))