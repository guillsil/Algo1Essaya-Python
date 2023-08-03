"""Mostrar los pasos del ordenamiento de la lista: 6 0 3 2 5 7 4 1 con los métodos
de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos? ¿Cuál
usarías en qué casos?"""
#lista = [6, 0, 3, 2, 5, 7, 4, 1]
#insercion
DEBUG:  [0, 6, 3, 2, 5, 7, 4, 1]
DEBUG:  [0, 3, 6, 2, 5, 7, 4, 1]
DEBUG:  [0, 2, 3, 6, 5, 7, 4, 1]
DEBUG:  [0, 2, 3, 5, 6, 7, 4, 1]
DEBUG:  [0, 2, 3, 5, 6, 7, 4, 1]
DEBUG:  [0, 2, 3, 4, 5, 6, 7, 1]
DEBUG:  [0, 1, 2, 3, 4, 5, 6, 7]
#merge sort
DEBUG:  [6, 0, 3, 2, 5, 7, 4, 1]
DEBUG:  [6, 0, 3, 2] [5, 7, 4, 1]
DEBUG:  [6, 0] [3, 2] [5, 7] [4, 1]
DEBUG:  [6] [0] [3] [2] [5] [7] [4] [1]
DEBUG:  [0, 6] [2, 3] [5, 7] [1, 4]
DEBUG:  [0, 2, 3, 6] [1, 4, 5, 7]
DEBUG:  [0, 1, 2, 3, 4, 5, 6, 7]