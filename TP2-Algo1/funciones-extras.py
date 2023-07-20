if linea.startswith("Level " + str(nivel)):
    for linea in archivo:
        if linea.startswith("Level "):
            return completar_grilla(desc)
        else:
            if linea.rstrip() != "":
                desc.append(linea.rstrip())

return completar_grilla(desc)

#leer niveles
try:
    nivel = nivel + 1
    desc = []
    with open(archivo_nivel) as archivo:
        # si el archivo esta vacio lanzar una excepcion
        if archivo.read() == "":
            raise ValueError("El archivo de niveles esta vacio")
        archivo.seek(0)
        for linea in archivo:
            if linea.startswith("Level " + str(nivel)):
                for linea in archivo:
                    if linea.startswith("Level "):
                        return desc
                    else:
                        if linea.rstrip() != "":
                            desc.append(linea.rstrip())

        return desc
except FileNotFoundError:
    raise FileNotFoundError("El archivo de niveles no existe")

def grilla_a_diccionario(grilla):
    """"devuelve un diccionario donde la clave es la posicion de cada elemento y el valor es el simbolo que representa"""
    diccionario = {}
    for i in range(len(grilla)):
        for j in range(len(grilla[i])):
            diccionario[grilla[i][j]] = LISTA_DE_SIMBOLOS[i]
    return diccionario


def imprimir_grilla(grilla):
    """Imprime la grilla"""
    diccionario = grilla_a_diccionario(grilla)
    for i in range(grilla[4][1]):
        for j in range(grilla[4][0]):
            if (j,i) in diccionario:
                print(diccionario[(j,i)], end="")
            else:
                print(" ", end="")
        print()

 """if tecla == "W" or tecla == "w" or tecla == "Up":
        movimiento = NORTE
        grilla = soko.mover(grilla, movimiento)
    elif tecla == "S" or tecla == "s" or tecla == "Down":
        movimiento = SUR
        grilla = soko.mover(grilla, movimiento)
    elif tecla == "A" or tecla == "a" or tecla == "Left":
        movimiento = OESTE
        grilla = soko.mover(grilla, movimiento)
    elif tecla == "D" or tecla == "d" or tecla == "Right":
        movimiento = ESTE
        grilla = soko.mover(grilla, movimiento)
    elif tecla == "Q" or tecla == "q":
        #tecla para reiniciar nivel
        grilla = soko.reiniciar_nivel(nivel)
    elif tecla == "E" or tecla == "e":
        #tecla para pasar de nivel
        nivel += 1
        grilla = soko.crear_grilla(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))
        max_col = soko.hallar_max_columnas(soko.completar_grilla(soko.leer_nivel("niveles.txt", nivel)))
        ancho_ventana = max_col * 60
        alto_ventana = grilla[4][1] * 60
        gamelib.resize(ancho_ventana, alto_ventana)
    else:
        print("Direccion invalida, intente nuevamente")
        return grilla
    """

def leer_nivel(archivo_nivel, nivel):
    """Busca el nivel solicitado en el archivo de niveles y lo devuelve como una lista de strings, no se debe devolver
    una línea vaciá al final"""
    try:
        with open(archivo_nivel, "r") as archivo:
            nivel = nivel + 1
            desc = []
            #si el archivo esta vacio o no existen lanzar una excepcion
            if archivo.read() == "":
                raise ValueError("El archivo de niveles esta vacio")
            for linea in archivo:
                if linea.startswith("Level " + str(nivel)):
                    for linea in archivo:
                        if linea.startswith("Level "):
                            return desc
                        else:
                            if linea != "":
                                desc.append(linea.rstrip())
            return desc
    except:
        raise ValueError("El archivo de niveles no existe")