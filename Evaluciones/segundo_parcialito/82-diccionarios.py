"""Se tiene un diccionario que guarda mensajes de un grupo, donde cada elemento tiene como clave un identificador,
y como valor otro diccionario con la información del mensaje:
{
    id: {
        'de': nombre de usuario que escribió,
        'texto': contenido del mensaje,
        'respuesta_a_id': id del mensaje al cual responde, o 0 si no le responde a nadie
    },
    . . .
}
Escribir una función contar_respuestas_a que recibe el diccionario de mensajes, una cadena usuario_destino y
devuelva un nuevo diccionario indicando la cantidad de respuestas que recibió por parte del resto de los usuarios
(la clave siendo el usuario, y valor la cantidad de respuestas)."""

def contar_respuestas_a(dic, usuario_destino):
    diccionario = {}
    for id in dic:
        if dic[id]['de'] == usuario_destino:
            if dic[id]['respuesta_a_id'] != 0:
                if dic[dic[id]['respuesta_a_id']]['de'] not in diccionario:
                    diccionario[dic[dic[id]['respuesta_a_id']]['de']] = 1
                else:
                    diccionario[dic[dic[id]['respuesta_a_id']]['de']] += 1
    return diccionario
