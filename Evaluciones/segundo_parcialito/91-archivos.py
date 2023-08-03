"""Se tiene una lista de los alumnos de una materia y se desea dividirlos en 3 grupos según resto del cociente
entre el padrón del alumno y 3.
    Si el padrón es $12345$, se deberá hacer $12345 % 3 = 2$
    Si el padrón es $7774$ se deberá hacer $7774 % 3 = 1$
    Si el padrón es $36$ se deberá hacer $36 % 3 = 0$
La lista de los alumnos se encuentra en un archivo que tiene un número de padrón por línea. Se pide escribir una
función que reciba por parámetro el nombre del archivo de alumnos y devuelva 3 archivos cuyos nombres tendrán
el formato: <nombre archivo alumnos>_Enunciado<número de grupo>.txt con la lista de padrones correspondientes a cada
grupo uno por línea.
Nota: al finalizar la ejecución de la función (haya ocurrido un error o no), todos los archivos abiertos deben
quedar cerrados"""
def dividir_alumnos(nombre_archivo):

    archivo = open(nombre_archivo, 'r')
    grupos = [[], [], []]
    for linea in archivo:
        padron = int(linea.strip())
        """saltear una linea luego de agregar un padron"""
        grupos[padron % 3].append(str(padron) + '\n')

    archivo.close()
    for i in range(3):
        archivo = open(nombre_archivo[:-4] + '_Enunciado{}.txt'.format(i + 1), 'w')
        for padron in grupos[i]:
            archivo.write(str(padron) + '')
        archivo.close()
print(dividir_alumnos('alumnos.txt'))


