# 11.★★Un nuevo regente del país "Atrasoñia" Ilegó al poder de la mano de 3 aliados. Como
# todo monarca decide repartir los puestos clave de poder para dejar contentos a todos ellos.
# Por otro lado, no desea que se formen cúmulos de poder que dificulten su dominio. Para
# ayudarse ha generado un diagrama donde se pueden ver los diferentes puestos y con qué
# otros puestos claves se relaciona. Lo que intenta es lograr que para cada par de puestos
# relacionados entre sí, las facciones que lo controlen sean diferentes. Existe un número total
# de relaciones entre puestos y lo que desea es que la mayor cantidad posible de ellos
# cumplan el criterio de "balanceo de poder"
# Proponer un algoritmo randomizado para lograr al menos del total posible de relaciones
# balanceados.


# es 3CG: coloreo de grafo con 3 colores, pero no de decisión, sino de minimización.
# montecarlo: mezclo la entradada de puestos y le voy asignando un color, que no este en sus 
# vecinos o cualuiqera de los otros si ya tiene vecinos con tres colores. Devuelvo el resultante.
# pros: polinomial. contras: no asegura optimidad.
# complejidad: O(n)

