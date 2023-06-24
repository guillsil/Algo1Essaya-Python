"""

Se tiene un archivo que guarda las notas de los alumnos de una materia, con formato:

padron,nombre,nota1;nota2;nota3;....

Se sabe que para cada alumno hay por lo menos una nota, pero no cuántas hay exactamente. Escribir una función que reciba la ruta a un archivo con ese formato y cree uno nuevo llamado promedios.csv con formato nombre;promedio, calculando dicho promedio a partir de las notas del alumno correspondiente.

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
import csv

def promedios(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo, open("promedios.csv", "w") as archivo2:
            archivo_reader = csv.reader(archivo)
            archivo_writer = csv.writer(archivo2)
            for padron, nombre, *notas in archivo_reader:
                calificacion = 0
                for nota in notas:
                    calificacion += int(nota)
                promedio = calificacion / len(notas)        
                archivo_writer.writerow([nombre, promedio])
    except FileNotFoundError:
        print("No se encontró el archivo")
        
promedios("notas.csv")

             
