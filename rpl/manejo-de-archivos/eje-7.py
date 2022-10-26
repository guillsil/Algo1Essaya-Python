"""a. Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido tiene el formato
clave,valor y devuelva un diccionario con el primer campo como clave y el segundo como lista.
b. Escribir una función guardar_datos que reciba un diccionario (con el mismo formato que la función anterior)
y un nombre de archivo, y guarde el contenido del diccionario en el archivo, con el formato clave,valor.
Nota: Como las dos funciones utilizan el mismo formato para el diccionario y el archivo, debería ser
posible llamar a guardar_datos y luego a cargar_datos para obtener el mismo diccionario.
Tomando por ejemplo el siguiente archivo:
The Godfather,Crime
The Dark Knight,Drama
The Dark Knight,Action
The Lord of the Rings: The Return of the King,Adventure
The Godfather,Action
Inception,Action
Inception,Sci-Fi
The Matrix,Action
The Lion King,Animation
The Matrix,Sci-Fi
Y el siguiente diccionario:
{
  'The Godfather': ['Crime', 'Action'],
  'The Dark Knight': ['Drama', 'Action'],
  'The Lord of the Rings: The Return of the King': ['Adventure'],
  'Inception': ['Action', 'Sci-Fi'],
  'The Matrix': ['Action', 'Sci-Fi'],
  'The Lion King': ['Animation']
}
Si el cargar_datos recibe la ruta a ese archivo, debe devolver ese diccionario. Si el guardar_datos recibe ese
diccionario, debe generar ese archivo sobre la ruta indicada"""
def cargar_datos(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    diccionario = {}
    for linea in archivo:
        clave, valor = linea.strip().split(',')
        if clave in diccionario:
            diccionario[clave].append(valor)
        else:
            diccionario[clave] = [valor]
    archivo.close()
    return diccionario
def guardar_datos(diccionario, nombre_archivo):
    archivo = open(nombre_archivo, 'w')
    for clave, valor in diccionario.items():
        for elemento in valor:
            archivo.write(f"{clave},{elemento},\n")
    archivo.close()

