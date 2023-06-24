"""Escribir una función que reciba el nombre de un archivo, el cual en cada línea tiene como información un nombre y una edad, separados por una coma. Devolver en forma de tupla la edad más alta y una lista de nombres de todas las personas que tienen dicha edad. Se puede recorrer el archivo sólo una vez.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv

def edadMasAlta(archivo):
    with open(archivo, "r") as file:
        reader = csv.reader(file)
        edadMasAlta = 0
        nombres = []
        for linea in reader:
            nombre, edad = linea
            edad = int(edad)
            if edad > edadMasAlta:
                edadMasAlta = edad
                nombres = [nombre]
            elif edad == edadMasAlta:
                nombres.append(nombre)
    return (edadMasAlta, nombres)

print(edadMasAlta("personas.csv"))