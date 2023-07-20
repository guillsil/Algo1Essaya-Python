"""Se tiene un archivo llamado socios.csv, con muchas líneas (es decir, no entra en memoria), de formato 
dni,nombre,edad,estado_civil,tiene_empleo,terminó_secundario, donde tiene_empleo y terminó_secundario son 0 si es falso y 1 si es verdadero. Escribir un programa que imprima (como se quiera) todos los datos de los no graduados del secundario, con empleo y que sean menores de 35 años. El archivo debe cerrarse en todos los casos, tanto cuando finaliza la ejecución normalmente como si hay algún error."""
import csv
EDADMAX = 35
def no_graduados(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            archivo_reader = csv.reader(archivo)
            for dni, nombre, edad, estado_civil, tiene_empleo, termino_secundario in archivo_reader:
                if int(edad) < EDADMAX and tiene_empleo == "1" and termino_secundario == "0":
                    print(f"{nombre} tiene {edad} años, es {estado_civil}, tiene empleo y no terminó el secundario")
    except FileNotFoundError:
        print("No se encontró el archivo")
    except ValueError:
        print("Error en el archivo")

no_graduados("socios.csv")


