"""1. 'Tras la crisis deportiva y econÓ1nica que atraviesa CI Club Atletico Independiente que ha a la renuncia
ele Fabián Doman a su cargo como presidente. IOS dirigentes estudian analizar dcportivrxs para tomar una (lecisión eon respecto al futuro del club.
como presidente. Los dirigentes estudian analizar los resultados deportivoss para tomar una (lecisión eon respecto al futuro del club.
Para ayudar a la dirigencia del club, se pide implementar una fición llamada rondimiontÓ que reciba corno parámetro una matriz de
" partidos' • que contiene la información de los resultados cada partido y (levuelva lista el rendimiento del equipo en
de las siguientes Total de puntos (+3 por gauulo, 81 pot partido empatado), Total de goles a favor. Total
de cn contra. Cada fila de la matriz de un p.rtido, la primer columna rcprcscnta cl rival. y la sczunda es una
tupla que representa el resultado en formato (goles _ propios. goles-rtvales). Por ejemplo;
[ k - Boca". (1.
("Racing". (O,
("River"""
# def resultadoPartido(golesAf, golesRi):
#     if golesAf > golesRi:
#         return 3
#     elif golesAf == golesRi:
#         return 1
#     else:
#         return 0
    
# partidos = [["Boca", (1,1)], ["Racing", (0,0)], ["River", (2,1)], ["San Lorenzo", (1,1)]]

# resultadoPartido(partidos[0][1][0], partidos[0][1][1])

# def rendimiento(partidos):
#     totalPuntos = 0
#     totalGolesFavor = 0
#     totalGolesContra = 0
#     listaPartidos = []
#     for partido in range(len(partidos)):
#         resultadoPartido(partidos[partido][1][0], partidos[partido][1][1])
#         totalPuntos += resultadoPartido(partidos[partido][1][0], partidos[partido][1][1])
#         totalGolesFavor += partidos[partido][1][0]
#         totalGolesContra += partidos[partido][1][1]
#     listaPartidos.append(totalPuntos)
#     listaPartidos.append(totalGolesFavor)
#     listaPartidos.append(totalGolesContra)
#     return listaPartidos

# print(rendimiento(partidos))

"""2, acuerdo el standard para representar telefónicos, números internacionales se representan de la siguiente manera:
de <codigo de arco telefonico separado espacios»
código de es y dc por 10 número 4187-6043 se representaría en la forma +54 11 4187
se una que reciba una listo de strings que código de Y
de atea. una lista solancntc con los números que a dicho país y arca. la respuesta
y area) y separando ei por guiones lugar de Por ejemplo, si recibiera los
Z: 6043', '+55 22 3332 5423'. '+54 11 4444 3343', 112 403 3202'
+54 13 4437 2233'
('4187-6043' 14444-3343')"""

CODIGOARGENTINA = "+54"
CODIGOBSAS = "11"

# def separarNumero(numero):
#     return numero.split("-")


# def extraerNumeroTelefonico(telefonos):
#     listaTelefonos = []
#     for telefono in telefonos:
#         numeroTelf = separarNumero(telefono)
#         if numeroTelf[0] == CODIGOARGENTINA and numeroTelf[1] == CODIGOBSAS:
#             listaTelefonos.append(numeroTelf[2] + " "  + numeroTelf[3])

#     return listaTelefonos

# telefonos = ["+54-11-4187-6043", "+55-22-3332-5423", "+54-11-4444-3343", "+54-13-4437-2233", "+54-11-403-3202"]
# print(extraerNumeroTelefonico(telefonos))

"""3- están cotnpuestas por secuencias, scparüas po: . dc dígitos que el f) A Por
¿ ger,erar chreccaon apv6() que una
et randotti y la ruc.ción randon. psrs
al una calitidiid
aleatoria linea, utilizando la antenor. ('l
.'iet,e la válido."""
import random

def generar_direccion_ipv6():
    direccion = ""
    for secuencia in range(8):
        for i in range(4):
            direccion += str(random.choice("0123456789abcdef")) 
        direccion += ":"
        if secuencia == 7:
            direccion = direccion[:-1]
        
    return direccion

print(generar_direccion_ipv6())



        


    


