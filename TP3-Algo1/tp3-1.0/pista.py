"""Presionando una tecla determinada (configurable mediante teclas.txt), el efecto dependerá de dos casos posibles:
No hay pistas disponibles: en este caso el juego intentará encontrar una solución al nivel, utilizando el algoritmo de
backtracking que se describe a continuación. Si se encuentra la solución, la sucesión de acciones correspondiente será
considerada como las pistas disponibles.
Hay pistas disponibles: Se desencola una pista y se efectúa esa acción, como si la hubiera hecho el jugador.
Si el jugador efectúa cualquier otra acción que no sea la acción de "pista", se debe descartar las pistas disponibles,
ya que no podemos asegurar que sean válidas para el estado actual."""
