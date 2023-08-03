"""Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
y el programa le debe decir a qué signo corresponde.
Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo."""
# a)
def signo(d, m):
    # Muestra en pantalla el signo del zodiaco de una fecha
    if (m == 1 and d >= 21) or (m == 2 and d <= 19):
        return "Acuario"
    elif (m == 2 and d >= 20) or (m == 3 and d <= 20):
        return "Piscis"
    elif (m == 3 and d >= 21) or (m == 4 and d <= 20):
        return "Aries"
    elif (m == 4 and d >= 21) or (m == 5 and d <= 20):
        return "Tauro"
    elif (m == 5 and d >= 21) or (m == 6 and d <= 21):
        return "Geminis"
    elif (m == 6 and d >= 22) or (m == 7 and d <= 23):
        return "Cancer"
    elif (m == 7 and d >= 24) or (m == 8 and d <= 23):
        return "Leo"
    elif (m == 8 and d >= 24) or (m == 9 and d <= 23):
        return "Virgo"
    elif (m == 9 and d >= 24) or (m == 10 and d <= 22):
        return "Libra"
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
        return "Escorpio"
    elif (m == 11 and d >= 23) or (m == 12 and d <= 21):
        return "Sagitario"
    elif (m == 12 and d >= 22) or (m == 1 and d <= 20):
        return "Capricornio"
    else:
        return "La fecha no es válida"
print(signo(31, 8))
