"""Suponiendo que el primer día del año fue lunes, escribir una función que reciba
un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por ejemplo:
si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'."""
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
def dia_semana(d):
    # Muestra en pantalla el día de la semana de un día del año el primer dia es un lunes
    return DIAS[d % 7 - 1]
assert dia_semana(3) == "miércoles"