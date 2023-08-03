"""Escribir una función que reciba una ruta a un archivo de pokemones con el siguiente formato <pokemon>;<tipo>;<pos_x>,<pos_y>,
y un diccionario de gimnasios (cada clave es el nombre de un gimnasio, y el valor asociado, su posicion, dada como una
tupla (pos_x, pos_y)) y escriba en un archivo de salida el pokemon, su tipo y su gimnasio más cercano. El archivo de
salida debe tener el siguiente formato: <pokemon;<tipo>;<gimnasio más cercano>.
Para calcular la distancia entre pokemon y gimnasio se utiliza distancia manhattan: dist(p1, p2) = |p1_x - p2_x| + |p1_y - p2_y|
Notas:
    El archivo no se encuentra ordenado bajo ningún criterio y no posee errores de formato ni de tipo de datos. No posee encabezado.
    El archivo puede recorrerse una única vez y no entra entero en memoria.

"""
def gimnasio_mas_cercano(pokemon, gimnasios):
    """Devuelve el gimnasio más cercano al pokemon, según la distancia manhattan.
    """
    archivo = open(pokemon, "r")
    archivo_salida = open("salida.txt", "w")
    for linea in archivo:
        linea = linea.strip()
        linea = linea.split(";")
        pokemon = linea[0]
        tipo = str(linea[1])
        pos_x = int(linea[2].split(",")[0])
        pos_y = int(linea[2].split(",")[1])
        distancia_minima = 0
        gimnasio_mas_cercano = ""
        for gimnasio in gimnasios:
            distancia = abs(pos_x - gimnasios[gimnasio][0]) + abs(pos_y - gimnasios[gimnasio][1])
            if distancia < distancia_minima:
                distancia_minima = distancia
                gimnasio_mas_cercano = gimnasio
        archivo_salida.write(f"{pokemon};{tipo};{gimnasio_mas_cercano}")
    archivo.close()
    archivo_salida.close()
print(gimnasio_mas_cercano("pokemones.txt", {"gimnasio1": (1, 1), "gimnasio2": (2, 2), "gimnasio3": (3, 3)}))