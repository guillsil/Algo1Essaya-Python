"""a) Dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
excepto que también sea divisible por 400."""
def esDivicible(num, div):
    # Muestra en pantalla si un número es divisible por otro
    return num % div == 0
# a)
def bisiesto(a):
    # Muestra en pantalla si un año es bisiesto
    cantidad_dias = 0
    return esDivicible(a, 4) and not esDivicible(a, 100) or esDivicible(a, 400)
assert bisiesto(2024) == True
"""b) Dado un mes y un año, devolver la cantidad de días correspondientes.
Nota: en febrero de un año bisiesto existen 29 días."""
# b)
def dias(m, a):
    # Muestra en pantalla la cantidad de días de un mes y año
    cantidad_dias = 0
    if m == 2:
        if bisiesto(a):
            cantidad_dias += 29
        else:
            cantidad_dias += 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        cantidad_dias += 30
    else:
        cantidad_dias += 31
    return cantidad_dias
assert dias(8, 2022) == 31
#c)Dada una fecha (día, mes, año), indicar si es válida o no.
def dia_valido(d, m, a):
    # Muestra en pantalla si un día es válido
    return (d > 0 and d <= dias(m, a))

assert dia_valido(31, 8, 2022) == True
#d)Dada una fecha, indicar los días que faltan hasta fin de mes.
def dias_faltantes(d, m, a):
    # Muestra en pantalla los días que faltan hasta fin de mes
    if dia_valido(d, m, a):
        return dias(m, a) - d
    else:
        return "El día no es válido"
assert dias_faltantes(31, 8, 2022) == 0