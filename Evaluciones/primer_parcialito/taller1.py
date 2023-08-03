'''
3) Escribir una funcion que dada una matriz representada
como una lista de listas de numeros
(donde cada sublista representa una fila),
devuelva una lista con los maximos de cada columna. 

Ejemplo:

maximos_columnas(
[
	[1, 2, 8, 4],
	[6, 7, 3, 3], ->  [6, 7, 8, 9]
	[6, 5, 4, 9]
]
)

'''

def maximos_columnas(matriz):
	maximos = []
	for j in range(len(matriz[0])):
		maximo = matriz[0][j] # max(fila)
		for i in range(len(matriz)):
			if maximo < matriz[i][j]:
				maximo = matriz[i][j]
		maximos.append(maximo)
	return maximos

'''
Escribir una funcion que imprima los numeros de 1 a 100;
pero para los multiplos de 3 imprima “Miki” en lugar del numero;
y para los multiplos de 5 imprima “Moko”. Para los
multiplos de 3 y 5 debe imprimir “MikiMoko”.

'''

def miki_moko():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print('MikiMoko')
		elif i % 3 == 0:
			print('Miki')
		elif i % 5 == 0:
			print('Moko')
		else:
			print(i)


'''
Escribir una funcion que pida cadenas al usuario hasta
que ingrese una cadena vacıa.
Debe devolver una lista de las palabras ingresadas. Por ejemplo:

Cadena: hola co
Cadena: mo
Cadena: estas ?
Cadena:

Debe devolver: [’hola’, ’como’, ’estas’, ’?’]
'''

def pedir_cadenas_v2():
	mensaje = ''
	while True:
		cadena = input('Cadena: ')
		if not cadena:
			return mensaje.split()
		mensaje += cadena

def pedir_cadenas():
	mensaje = ''
	cadena = input('Cadena: ')
	while cadena != '':
		mensaje += cadena
		cadena = input('Cadena: ')
	return mensaje.split()

'''
Un bigrama es una secuencia de dos palabras contiguas dentro de un texto.
Escribir una función que reciba un texto y devuelva una lista con
todos sus bigramas.
Los mismos deberán estar representados con una tupla (, ).

Ejemplo:

obtener_bigramas("Uno se alegra de resultar útil")
[('Uno', 'se'), ('se', 'alegra'), ('alegra', 'de'), ('de', 'resultar'), ('resultar', 'útil')]

'''

def obtener_bigramas(texto):
	palabras = texto.split()
	bigramas = []
	for i in range(len(palabras) - 1):
		bigrama = (palabras[i], palabras[i + 1])
		bigramas.append(bigrama)
	return bigramas

'''

Escribir una funcion que reciba por
parametro una lista de numeros y devuelva otra lista
con los numeros de la ingresada que terminan en cero.

Por ejemplo, si se recibe la lista: 
[4, 23, 40, -7, 0, 14, 1000, -760] debe devolver [40, 0, 1000, -760].

'''

def filtrar_multiplos_de_10(numeros):
	multiplos = []
	for numero in numeros:
		if numero % 10 == 0:
			multiplos.append(numero)
	return multiplos

def filtrar_multiplos_de_10_v2(numeros):
	return list(filter(lambda numero: numero % 10 == 0, numeros))

def imprimir_ordenados_por_columna(numeros, n):
	columnas = []
	for i in range(0, len(numeros), n):
		columnas.append(numeros[i:i+n])

	for j in range(len(columnas[0])):
		for i in range(len(columnas)):
			if j < len(columnas[i]):
				print(columnas[i][j], end=" ")
		print()

def es_curioso(numero):
	return str(numero ** 2)[-len(str(numero)):] == str(numero)

def imprimir_primeros_n_curiosos(n):
	numero = 0
	while n > 0:
		if es_curioso(numero):
			print(numero)
			n -= 1
		numero += 1


'''
Escribir una funcion dar_vuelta que reciba una lista de tuplas
de numeros y que devuelva una nueva lista de tuplas,
donde la primer tupla tendra el primer elemento de
todas las tuplas originales; la segunda, los segundos, etc.

Ejemplo:

[(1,2,3), (4,5), (6,), (7,8,9,10)]
  => 
[(1,4,6,7), (2,5,8), (3,9), (10,)]

Nota: las tuplas originales no tienen todas la misma
cantidad de elementos entre sí.

Ayuda: una tupla de un solo elemento se puede crear de la forma t = (elem,)

'''

def max_por_len_v2(lista):
	maximo = len(lista[0])
	for elemento in lista:
		if len(elemento) > maximo:
			maximo = len(elemento)
	return maximo

def max_por_len(lista):
	return len(max(lista, key=len))

def dar_vuelta(tuplas):
	dadas_vuelta = []
	for j in range(max_por_len(tuplas)):
		tupla = ()
		for i in range(len(tuplas)):
			if j < len(tuplas[i]):
				tupla += (tuplas[i][j],)
		dadas_vuelta.append(tupla)
	return dadas_vuelta
