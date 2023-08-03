"""Se tienen dos archivos cuyos campos son DNI,Apellido,Nombre, y están ordenados por DNI. Escribir una
función que reciba los nombres de dos archivos como los mencionados, y genere un nuevo archivo que incluya
los datos de ambos archivos de entrada, también ordenados por DNI y sin duplicados.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos
deben quedar cerrados.
"""
def f_a_d_d(archivo1, archivo2):
    try:
        archivo1 = open(archivo1, "r")
        archivo2 = open(archivo2, "r")
        archivo3 = open("archivo3.txt", "w")
        archivo1.readline()
        archivo2.readline()
        archivo3.write("DNI,Apellido,Nombre")
        #los dni no se deben repetir en el archivo3
        dni = []
        for linea in archivo1:
            linea = linea.strip()
            linea = linea.split(",")
            if linea[0] not in dni:
                dni.append(linea[0])
                archivo3.write(f"{linea[0]},{linea[1]},{linea[2]}")
        for linea in archivo2:
            linea = linea.strip()
            linea = linea.split(",")
            if linea[0] not in dni:
                dni.append(linea[0])
                archivo3.write(f"{linea[0]},{linea[1]},{linea[2]}")
        archivo1.close()
        archivo2.close()
        archivo3.close()
        return "Archivo3.txt creado"
    except:
        archivo1.close()
        archivo2.close()
        archivo3.close()
        return "Error"
