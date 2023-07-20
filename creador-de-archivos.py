def crear_archivos(n, tema):
    #crear n archivos .py con el formato eje-{numero}.py
    for i in range(1, n+1):
        archivo = open(f"{tema}-eje-{i}.py", 'w')
        archivo.close()
crear_archivos(5, 'Objetos')