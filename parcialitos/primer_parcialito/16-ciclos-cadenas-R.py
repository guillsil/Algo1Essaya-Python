"""Se quiere implementar un algoritmo simple de código de control que haga lo siguiente: a partir de un número de
N dígitos, y separado por un guión al final se encuentra el dígito verificador. El mismo se obtiene a partir de
hacer la suma de los dígitos previos al - y a esa suma aplicarle módulo 10.
Por ejemplo para el código '4597-5' el número es '4597' y el verificador es 5. Para validarlo, se suman los dígitos
del número resultando en 25, y el módulo 10 del mismo da 5. Como obtuvimos el mismo valor que el dígito verificador,
el código es válido.
Escribir una función que dado un código indique si es válido.
Ejemplos:
'4597-5' -> Valido
'4597-6' -> Invalido
'12345-5' -> Valido"""

def validar_codigo(codigo):
    """Indica si el código es válido."""
    numero, verificador = codigo.split('-')
    return sum(map(int, numero)) % 10 == int(verificador) # map(int, numero) devuelve una lista de enteros #sum() suma los elementos de una lista
print(validar_codigo('4597-5'))
print(validar_codigo('4597-6'))
print(validar_codigo('12345-5'))
