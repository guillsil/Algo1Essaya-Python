def obtener_nivel(archivo_nivel):
    """Lee el archivo de niveles y devuelve una lista con los niveles donde cada nivel es una lista de strings"""
    try:
        niveles = []
        with open(archivo_nivel) as archivo:
            desc = []
            for linea in archivo:
                for nivel in range(MAX_LEVEL):
                    if linea.startswith("Level " + str(nivel)):
                        for linea in archivo:
                            if linea.startswith("Level "):
                                niveles.append(completar_grilla(desc))
                                desc = []

                            else:
                                if linea.rstrip() != "":
                                    desc.append(linea.rstrip())
                        niveles.append(completar_grilla(desc))
        return niveles
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de niveles no existe")
print(obtener_nivel("niveles.txt")[153])