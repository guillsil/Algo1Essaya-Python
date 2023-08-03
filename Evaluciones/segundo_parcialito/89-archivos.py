"""Escribir una función que reciba el nombre de un archivo, el cual en cada línea tiene como información un
nombre y una edad, separados por una coma. Devolver en forma de tupla la edad más alta y una lista de nombres
de todas las personas que tienen dicha edad. Se puede recorrer el archivo sólo una vez.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben
quedar cerrados.
"""
def nombres_y_edades(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    max_edad = 0
    nombres = []
    for linea in archivo:
        datos = linea.strip().split(',')
        edad = int(datos[1])
        if edad > max_edad:
            max_edad = edad
            nombres = [datos[0]]
        elif edad == max_edad:
            nombres.append(datos[0])
    archivo.close()
    return (max_edad, nombres)
print(nombres_y_edades('nombres.csv'))