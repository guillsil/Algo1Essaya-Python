""". Persistencia de un diccionario
a) Escribir una función cargar_datos que reciba un nombre de archivo, cuyo contenido
tiene el formato clave, valor y devuelva un diccionario con el primer campo como clave
y el segundo como diccionario.
b) Escribir una función guardar_datos que reciba un diccionario y un nombre de archivo,
y guarde el contenido del diccionario en el archivo, con el formato clave, valor."""
#recibe archivo3.txt
def cargar_datos(archivo):
    diccionario = {}
    with open(archivo, 'r') as f:
        for linea in f:
            lista = linea.split(',')
            diccionario[lista[0]] = lista[1].strip()

    return diccionario
print(cargar_datos('archivo3.txt'))