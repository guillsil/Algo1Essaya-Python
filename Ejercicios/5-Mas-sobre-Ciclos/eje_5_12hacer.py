"""Escribir una función que dada la cantidad de ejercicios de un examen, y el por-
centaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, revise un
grupo de examenes. Para ello, en cada paso debe preguntar la cantidad de ejercicios resueltos
por el alumno, indicando con un valor centinela que no hay más examenes a revisar. Debe mos-
trar por pantalla el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la
cantidad de ejercicios del examen y una leyenda que indique si aprobó o no."""
CANTIDAD_EJERCICIOS = 10
PORCENTAJE_APROBACION = 0.6
def examen(ejercicios, porcentaje):
    while ejercicios != 0:
        if ejercicios / CANTIDAD_EJERCICIOS >= porcentaje:
            aprobados += 1
        else:
            reprobados += 1
        ejercicios = int(input("Ingrese la cantidad de ejercicios resueltos: "))
    print("Aprobados: ", aprobados)
    print("Reprobados: ", reprobados)
