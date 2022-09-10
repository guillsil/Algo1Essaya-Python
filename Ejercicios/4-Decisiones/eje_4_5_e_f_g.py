import eje_4_5_a_b_c_d
#e)Dada una fecha, indicar los días que faltan hasta fin de año.
def dias_faltantes_ano(d, m, a):
    # Muestra en pantalla los días que faltan hasta fin de año
    if eje_4_5_a_b_c_d.dia_valido(d, m, a):
        dias_faltantes = 0
        for i in range(m, 13):
            dias_faltantes += eje_4_5_a_b_c_d.dias(i, a)
        return dias_faltantes - d
    else:
        return "El día no es válido"

#f)Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
def dias_transcurridos(d, m, a):
    # Muestra en pantalla la cantidad de días transcurridos en un año hasta una fecha
    return 365 - dias_faltantes_ano(d, m, a)
assert dias_transcurridos(30, 12, 2022) == 364
"""g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
entre ambas, en años, meses y días.
6
Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
"""
def tiempo_transcurrido(d1, m1, a1, d2, m2, a2):
    # Muestra en pantalla el tiempo transcurrido entre dos fechas
    return abs(a1 - a2), abs(m1 - m2), abs(d1 - d2)














