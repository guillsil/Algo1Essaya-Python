"""Se tiene un archivo con el siguiente formato <nombre persona>;<lugar>;<momento en que la persona estuvo
alli>.hEscribir una funcion que reciba la ruta a este archivo y el nombre de una persona y devuelva un conjunto con
todas las personas con las que tuvo contacto. Una persona tuvo contacto con otra si estuvieron en el mismo lugar en
el mismo momento).
Notas:
El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos.
No posee encabezado.
El archivo puede recorrerse una única vez.
Cada persona puede haber estado en multiples lugares en múltiples momentos distintos (inclusive múltiples momentos
para el mismo lugar).
El tipo de dato para el "momento" no importa, tratarlo como una cadena."""
def personas_en_un_mismo_momento(nombre_archivo, nombre_persona):
    archivo = open(nombre_archivo, 'r')
    personas = []
    dic_personas = {}
    for linea in archivo:
        datos = linea.strip().split(';')
        if datos[0] == nombre_persona:
            dic_personas[datos[1]] = datos[2]
        elif datos[1] in dic_personas:
            if datos[2] == dic_personas[datos[1]]:
                personas.append(datos[0])
    archivo.close()
    return (personas)
print(personas_en_un_mismo_momento('contactos.csv', 'Guillermo'))

