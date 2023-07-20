"""Escribir una función que reciba la ruta a un archivo de texto, y devuelva el promedio del largo de las palabras de dicho texto (considerando signos de puntuación y otros símbolos como parte de la palabra).

Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben quedar cerrados.
"""
def promedioLargoPalabras(ruta_archivos):
    total_palabras = 0
    total_largo_palabras = 0
    try:
        with open(ruta_archivos, "r") as file:
            linea = file.readline()
            palabras = linea.split()
            for palabra in palabras:
                total_palabras += len(palabra)
                total_largo_palabras += sum(len(palabra) for palabra in palabras)
                
    except FileNotFoundError:
        
        return print("No se encontró el archivo")
    except:
        
        return print("Error inesperado")
    
    if total_palabras > 0:
        return total_largo_palabras / total_palabras 
    else:
        return 0.0
    
print(promedioLargoPalabras("texto.txt"))
