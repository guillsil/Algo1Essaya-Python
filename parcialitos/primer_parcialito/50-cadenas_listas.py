"""Escribir una función que dada una práctica y una lista de alumnos y su práctica asignada, devuelva
todos los nombres de los alumnos asignados a la práctica recibido. Ejemplo: Dada la práctica "Grace"
y los alumnos: [(103456, "Juan", "Pérez", "Grace"), (103333, "Marta", "López", "Bárbara"),
(103692, "Diana", "Rodríguez", "Grace"), (99264, "Pepito", "Martínez", "Alan")]"""
def alumnos_practica(practica, alumnos):
    lista_alumnos = []
    for alumno in alumnos:
        if alumno[3] == practica:
            lista_alumnos.append(alumno[1] + " " + alumno[2])
    return lista_alumnos
print(alumnos_practica("Alan", [(103456, "Juan", "Pérez", "Grace"), (103333, "Marta", "López", "Bárbara"), (103692, "Diana", "Rodríguez", "Grace"), (99264, "Pepito", "Martínez", "Alan")]))