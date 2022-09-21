"""En cierto concurso, el ganador se elige de entre los participantes colocandolos en fila y siguiendo estos pasos:
Se elimina al primer participante de la fila, y se sigue eliminando de dos en dos hasta el final (el segundo no,
el tercero si, el cuarto no, el quinto si, etc).
Al llegar al final, se repite el proceso a la inversa con los participantes que quedan. Se elimina el ultimo que quedo
(luego de quitar a los del paso anterior) y se sigue eliminando de dos en dos hasta llegar al principio.
Se repiten los pasos 1 y 2 hasta que quede un único participante, que sera el ganador.
Escribir una función elegir_participante que reciba una lista de participantes (que representa la fila) y devuelva el participante ganador.

Ejemplo: Si hay 10 participantes: [0,1,2,3,4,5,6,7,8,9] Después de la primer pasada quedan [1, 3, 5, 7, 9]
 (se eliminan el 0,2,4,6,8) Después de la segunda pasada quedan [3, 7] (se eliminan el 9,5,1) Después de la
 tercer pasada queda [7] (se elimina el 3) El participante elegido es el 7.
"""
